from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from models.bird_info import Bird_info
from config.database import collection_name, db
from schemas.schemas import list_serial, individual_serial
from pymongo.errors import DuplicateKeyError
import os
from typing import List
import base64
import numpy as np
import pandas as pd
import librosa
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
import joblib
from pydub import AudioSegment
from pydub.utils import audioop
from pymongo import ASCENDING
from bson.json_util import dumps


router = APIRouter() 


label_to_class_label = {15: 'Gallinula chloropus_Common Moorhen',
 8: 'Eudynamys scolopaceus_Asian Koel',
 34: 'Recurvirostra avosetta_Pied Avocet',
 2: 'Charadrius dubius_Little Ringed Plover',
 30: 'Rallus aquaticus_Water Rail',
 17: 'Calidris alpina_Dunlin',
 24: 'Pluvialis squatarola_Grey Plover',
 25: 'Tringa glareola_Wood Sandpiper',
 6: 'Gallinago gallinago_Common Snipe',
 3: 'Tringa totanus_Common Redshank',
 5: 'Amaurornis phoenicurus_White-breasted Waterhen',
 4: 'Haematopus ostralegus_Eurasian Oystercatcher',
 10: 'Columba palumbus_Common Wood Pigeon',
 22: 'Hirundo rustica_Barn Swallow',
 23: 'Limosa limosa_Black-tailed Godwit',
 14: 'Tringa ochropus_Green Sandpiper',
 9: 'Acridotheres tristis_Common Myna',
 11: 'Apus apus_Common Swift',
 7: 'Grus grus_Common Crane',
 1: 'Corvus macrorhynchos_Large-billed Crow',
 18: 'Coturnix coturnix_Common Quail',
 27: 'Porzana porzana_Spotted Crake',
 31: 'Psittacula krameri_Rose-ringed Parakeet',
 36: 'Scolopax rusticola_Eurasian Woodcock',
 21: 'Himantopus himantopus_Black-winged Stilt',
 28: "Zapornia pusilla_Baillon's Crake",
 12: 'Arenaria interpres_Ruddy Turnstone',
 35: 'Tachybaptus ruficollis_Little Grebe',
 19: 'Charadrius hiaticula_Common Ringed Plover',
 13: 'Fulica atra_Eurasian Coot',
 20: 'Caprimulgus macrurus_Large-tailed Nightjar',
 29: 'Numenius arquata_Eurasian Curlew',
 32: 'Orthotomus sutorius_Common Tailorbird',
 33: 'Podiceps cristatus_Great Crested Grebe',
 0: 'Cuculus canorus_Common Cuckoo',
 26: 'Numenius phaeopus_Eurasian Whimbrel',
 16: 'Actitis hypoleucos_Common Sandpiper'}


def extract_features(audio_part, target_sr=16000):
    try:

        chroma_stft = librosa.feature.chroma_stft(y=audio_part, sr=target_sr)
        mfccs = librosa.feature.mfcc(y=audio_part, sr=target_sr, n_mfcc=13)
        spectral_centroid = librosa.feature.spectral_centroid(y=audio_part, sr=target_sr)
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=audio_part, sr=target_sr)
        spectral_rolloff = librosa.feature.spectral_rolloff(y=audio_part, sr=target_sr)
        rmse = librosa.feature.rms(y=audio_part)
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y=audio_part)

        features = {
            'chroma_stft': chroma_stft,
            'mfccs': mfccs,
            'spectral_centroid': spectral_centroid,
            'spectral_bandwidth': spectral_bandwidth,
            'spectral_rolloff': spectral_rolloff,
            'rmse': rmse,
            'zero_crossing_rate': zero_crossing_rate,
        }
        return features

    except Exception as e:
        print(f"Error extracting features: {e}")
        return None


def extract_features_for_prediction(audio_file_path):
    try:
        y, sr = librosa.load(audio_file_path, sr=16000, mono=True)
        y_preemphasized = librosa.effects.preemphasis(y)

        features_for_prediction = extract_features(y_preemphasized)

        if features_for_prediction is not None:
            aggregated_mfcc = np.mean(features_for_prediction['mfccs'], axis=1)
            aggregated_chroma = np.mean(features_for_prediction['chroma_stft'], axis=1)
            aggregated_other = [
                np.mean(features_for_prediction['spectral_centroid']),
                np.mean(features_for_prediction['spectral_bandwidth']),
                np.mean(features_for_prediction['spectral_rolloff']),
                np.mean(features_for_prediction['rmse']),
                np.mean(features_for_prediction['zero_crossing_rate'])
            ]

            feature_vector = np.concatenate([aggregated_mfcc, aggregated_chroma, aggregated_other])

            if len(feature_vector) == 30:
                return feature_vector
            else:
                print(f"Error: Incorrect number of features in the aggregated feature vector")
                return None

    except Exception as e:
        print(f"Error extracting features for prediction: {e}")
        return None


def create_csv_for_audio_file(audio_file_path):
    scaler = joblib.load('routes/scaler.joblib')
    column_names = [
        f'mfcc_{i}' for i in range(1, 14)
    ] + [
        f'chroma_{i}' for i in range(1, 13)
    ] + [
        'spectral_centroid', 'spectral_bandwidth', 'spectral_rolloff', 'rmse', 'zero_crossing_rate'
    ]

    data = []

    feature_vector = extract_features_for_prediction(audio_file_path)

    if feature_vector is not None:
        data.append(feature_vector)

    df = pd.DataFrame(data, columns=column_names)
    bird_model = load_model('routes/FinalBirdModel.h5')
    corresponding_class_label = label_to_class_label.get(np.argmax(bird_model.predict(scaler.transform(df))), "Unknown")
    print(np.argmax(bird_model.predict(scaler.fit_transform(df))))
    return corresponding_class_label




# for getting the basic bird info
@router.get("/bird_info")
async def get_birds():
    bird_infos = list_serial(collection_name.find())
    return bird_infos


# adding data in database
@router.post("/add_bird", response_model=Bird_info)
async def add_bird_info(bird_info: Bird_info):
    try:
       collection_name.insert_one(dict(bird_info))
        
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Bird with the same name already exists")
    


@router.get("/get_bird/{bird_name}", response_model=Bird_info)
async def get_bird_info(bird_name: str):
    bird_info = collection_name.find_one({ "name": { "$regex": bird_name, "$options": "i" } })

    if bird_info is None:
        raise HTTPException(status_code=404, detail="Bird not found")
    
    return individual_serial(bird_info)



#for receiving audio file from application
@router.post("/process_audio/")
async def process_audio(audio_file: UploadFile):

    file_path = os.path.join(os.getcwd(), "uploaded_audio.wav")
    with open("uploaded_audio.wav", "wb") as f:
        f.write(audio_file.file.read())

    bird = create_csv_for_audio_file(file_path)

    os.remove(file_path)

    results = {"result": bird}
    return JSONResponse(content=results)
    

    

@router.get("/get_bird_audio/{audio_name}")
async def get_bird_audio(audio_name: str):
    audio_folder_path = os.path.join("./assets/","audio")
    audio_path = os.path.join(audio_folder_path, f"{audio_name}.mp3")

    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg")
    
    else:
        raise HTTPException(status_code=404, detail="audio not found")
    


@router.post("/favourite/{bird_name}/{user_name}")
async def post_favourite(bird_name: str, user_name: str):
    try:
        user_collection_name = f"{user_name}_favourites"
        collection = db[user_collection_name]
        collection.create_index([("bird", ASCENDING)], unique=True)
        document = {"bird": bird_name}
        result = collection.insert_one(document)
        return JSONResponse(content={"status": "success", "document_id": str(result.inserted_id)})

    except Exception as e:
        if "E11000 duplicate key" in str(e):
            return JSONResponse(content={"status" : "data already present"})
        else:
            raise HTTPException(status_code=500, detail=str(e))
        

def individual_serial_fav(fav_birds) -> dict:
    return {
        "id": str(fav_birds["_id"]),
        "bird" : str(fav_birds["bird"])
        
    }
        

@router.get("/get_favourite_birds/{user_name}")
async def get_favourite(user_name: str):
    try:
        user_collection_name = f"{user_name}_favourites"
        collection = db[user_collection_name]
        fav_birds = list(collection.find())
        fav_birds_dict = [individual_serial_fav(bird) for bird in fav_birds]
        return fav_birds_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_favourite_birds/{user_name}/{bird_name}")
async def del_favourite(user_name: str, bird_name: str):
    user_collection_name = f"{user_name}_favourites"
    collection = db[user_collection_name]
    deleted_item = collection.find_one_and_delete({"bird": bird_name})

    if deleted_item is not None:
        if '_id' in deleted_item:
            deleted_item['_id'] = str(deleted_item['_id'])
        return deleted_item
    else:
        raise HTTPException(status_code=404, detail="Item not found")




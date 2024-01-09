from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from models.bird_info import Bird_info
from config.database import collection_name
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


router = APIRouter() 


label_to_class_label = {31: 'Porzana porzana_Spotted Crake',
 0: 'Cuculus canorus_Common Cuckoo',
 27: 'Amaurornis phoenicurus_White-breasted Waterhen',
 34: 'Apus apus_Common Swift',
 41: 'Gallinula chloropus_Common Moorhen',
 8: 'Corvus splendens_House Crow',
 45: 'Caprimulgus macrurus_Large-tailed Nightjar',
 47: 'Centropus sinensis_Greater Coucal',
 23: 'Psilopogon virens_Great Barbet',
 38: 'Podiceps cristatus_Great Crested Grebe',
 36: 'Rallus aquaticus_Water Rail',
 12: 'Milvus migrans_Black Kite',
 30: 'Grus grus_Common Crane',
 9: 'Mulleripicus pulverulentus_Great Slaty Woodpecker',
 43: 'Coturnix coturnix_Common Quail',
 32: "Zapornia pusilla_Baillon's Crake",
 40: 'Fulica atra_Eurasian Coot',
 14: 'Halcyon smyrnensis_White-throated Kingfisher',
 25: 'Pavo cristatus_Indian Peafowl',
 46: 'Cacomantis merulinus_Plaintive Cuckoo',
 16: 'Eudynamys scolopaceus_Asian Koel',
 29: 'Halcyon smyrnensis_White-throated Kingfisher',
 4: 'Otus spilocephalus_Mountain Scops Owl',
 21: 'Orthotomus sutorius_Common Tailorbird',
 18: 'Columba palumbus_Common Wood Pigeon',
 15: 'Taenioptynx brodiei_Collared Owlet',
 2: 'Hirundo rustica_Barn Swallow',
 6: 'Phoenicurus auroreus_Daurian Redstart',
 20: 'Psittacula krameri_Rose-ringed Parakeet',
 10: 'Clangula hyemalis_Long-tailed Duck',
 42: 'Spilopelia senegalensis_Laughing Dove',
 33: 'Hierococcyx sparverioides_Large Hawk-Cuckoo',
 22: 'Spilopelia chinensis_Spotted Dove',
 11: 'Dendrocitta formosae_Grey Treepie',
 3: 'Corvus macrorhynchos_Large-billed Crow',
 26: 'Circus aeruginosus_Western Marsh Harrier',
 39: 'Cuculus micropterus_Indian Cuckoo',
 44: 'Tachybaptus ruficollis_Little Grebe',
 7: 'Emberiza rustica_Rustic Bunting',
 28: 'Columba livia_Rock Dove',
 17: 'Acridotheres tristis_Common Myna',
 35: 'Gallus gallus_Red Junglefowl',
 24: 'Passer domesticus_House Sparrow',
 37: 'Elanus caeruleus_Black-winged Kite',
 5: 'Dicrurus macrocercus_Black Drongo',
 13: 'Dendrocitta vagabunda_Rufous Treepie',
 19: 'Urocissa erythroryncha_Red-billed Blue Magpie',
 1: 'Nisaetus cirrhatus_Changeable Hawk-Eagle'}



#for audio preprocessing
def process_audio_generator(file_path, duration=5, target_sr=16000):
    try:
        y, sr = librosa.load(file_path, sr=target_sr)
        y_preemphasized = librosa.effects.preemphasis(y)

        samples_per_part = int(duration * target_sr)
        num_segments = len(y_preemphasized) // samples_per_part

        for i in range(num_segments):
            audio_part = y_preemphasized[i * samples_per_part : (i + 1) * samples_per_part]
            yield audio_part

    except Exception as e:
        print(f"Error processing {file_path}: {e}")



def aggregate_features(features):
    aggregated_features = {}
    
    for feature_name, feature_value in features.items():
        aggregated_feature = np.mean(feature_value, axis=1)
        aggregated_features[feature_name] = aggregated_feature

    return aggregated_features


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
        y, sr = librosa.load(audio_file_path, sr=16000)
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

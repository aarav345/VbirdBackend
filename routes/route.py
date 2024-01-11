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
from pydub import AudioSegment
from pydub.utils import audioop
import io

router = APIRouter() 


label_to_class_label = {31: 'Spotted Crake',
 0: 'Common Cuckoo',
 27: 'White-breasted Waterhen',
 34: 'Common Swift',
 41: 'Common Moorhen',
 8: 'House Crow',
 45: 'Large-tailed Nightjar',
 47: 'Greater Coucal',
 23: 'Great Barbet',
 38: 'Great Crested Grebe',
 36: 'Water Rail',
 12: 'Black Kite',
 30: 'Common Crane',
 9: 'Great Slaty Woodpecker',
 43: 'Common Quail',
 32: "Baillon's Crake",
 40: 'Eurasian Coot',
 14: 'White-throated Kingfisher',
 25: 'Indian Peafowl',
 46: 'Plaintive Cuckoo',
 16: 'Asian Koel',
 29: 'White-throated Kingfisher',
 4: 'Mountain Scops Owl',
 21: 'Common Tailorbird',
 18: 'Common Wood Pigeon',
 15: 'Collared Owlet',
 2: 'Barn Swallow',
 6: 'Daurian Redstart',
 20: 'Rose-ringed Parakeet',
 10: 'Long-tailed Duck',
 42: 'Laughing Dove',
 33: 'Large Hawk-Cuckoo',
 22: 'Spotted Dove',
 11: 'Grey Treepie',
 3: 'Large-billed Crow',
 26: 'Western Marsh Harrier',
 39: 'Indian Cuckoo',
 44: 'Little Grebe',
 7: 'Rustic Bunting',
 28: 'Rock Dove',
 17: 'Common Myna',
 35: 'Red Junglefowl',
 24: 'House Sparrow',
 37: 'Black-winged Kite',
 5: 'Black Drongo',
 13: 'Rufous Treepie',
 19: 'Red-billed Blue Magpie',
 1: 'Changeable Hawk-Eagle',
 47: 'Noise'}


# for processing audio
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

    audio_content = audio_file.file.read()

    if audio_file.content_type != 'audio/mp3':
        audio = AudioSegment.from_file(io.BytesIO(audio_content), format=audio_file.content_type)
        audio_content = audio.export(format='mp3').read()

    bird = create_csv_for_audio_file(io.BytesIO(audio_content))

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

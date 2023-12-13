from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from models.bird_info import Bird_info
from config.database import collection_name
from schemas.schemas import list_serial, individual_serial
from pymongo.errors import DuplicateKeyError
import os
from typing import List
import base64



router = APIRouter()    


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
    

# case insensitive search
@router.get("/get_bird/{bird_name}", response_model=Bird_info)
async def get_bird_info(bird_name: str):
    # Find the bird data in the MongoDB collection based on the name
    bird_info = collection_name.find_one({ "name": { "$regex": bird_name, "$options": "i" } })

    if bird_info is None:
        raise HTTPException(status_code=404, detail="Bird not found")
    
    return individual_serial(bird_info)



#for receiving audio file from application
@router.post("/process_audio/")
async def process_audio(audio_file: UploadFile):
    with open("uploaded_audio.wav", "wb") as f:
        f.write(audio_file.file.read())

    results = {"result": "data stored in api"}
    return JSONResponse(content=results)
    

    

@router.get("/get_bird_audio/{audio_name}")
async def get_bird_audio(audio_name: str):
    audio_folder_path = os.path.join("./assets/","audio")
    audio_path = os.path.join(audio_folder_path, f"{audio_name}.mp3")

    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg")
    
    else:
        raise HTTPException(status_code=404, detail="audio not found")

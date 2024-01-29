from pydantic import BaseModel
from typing import Optional

   

class Bird_info(BaseModel):
    name:str
    length:str
    wingspan:str
    mass:str
    scientificName: str
    description:str
    location:str
    audio:str
    imageUri: str
    video:str




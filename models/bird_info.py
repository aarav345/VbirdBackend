from pydantic import BaseModel
from typing import Optional

   

class Bird_info(BaseModel):
    name:str
    scientificName: str
    description:str
    location:str
    imageUri: str


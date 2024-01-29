def individual_serial(bird_info) -> dict:
    return {
        "id": str(bird_info["_id"]),
        "name": str(bird_info["name"]),
        "length" : str(bird_info["length"]),
        "wingspan": str(bird_info["wingspan"]),
        "mass" : str(bird_info["mass"]),
        "scientificName": str(bird_info["scientificName"]),
        "description": str(bird_info["description"]),
        "location" : str(bird_info["location"]),
        "audio" : str(bird_info["audio"]),
        "imageUri": str(bird_info["imageUri"]),
        "video" : str(bird_info["video"])

    }


def list_serial(bird_infos) -> list:
    return [individual_serial(bird_info) for bird_info in bird_infos]
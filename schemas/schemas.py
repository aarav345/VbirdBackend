def individual_serial(bird_info) -> dict:
    return {
        "id": str(bird_info["_id"]),
        "name": str(bird_info["name"]),
        "scientificName": str(bird_info["scientificName"]),
        "description": str(bird_info["description"]),
        "location" : str(bird_info["location"]),
        "imageUri": str(bird_info["imageUri"])
    }


def list_serial(bird_infos) -> list:
    return [individual_serial(bird_info) for bird_info in bird_infos]
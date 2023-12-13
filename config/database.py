from pymongo.mongo_client import MongoClient




client = MongoClient("mongodb+srv://admin:Aaswon1%4034@cluster0.umdlv7g.mongodb.net/?retryWrites=true&w=majority")

db = client.bird_info

collection_name = db["bird_collection"]








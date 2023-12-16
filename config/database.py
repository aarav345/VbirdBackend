from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    # Connect to the MongoDB Atlas cluster
    client = MongoClient("mongodb+srv://admin:Aaswon1%4034@cluster0.umdlv7g.mongodb.net/?retryWrites=true&w=majority")

    # Access the 'bird_info' database and the 'bird_collection' collection
    db = client.bird_info
    collection_name = db["bird_collection"]

    # Check if the connection is successful
    if client.server_info():
        print("Connected to MongoDB Atlas")
    else:
        print("Failed to connect to MongoDB Atlas")

except ConnectionFailure as e:
    print(f"Error connecting to MongoDB Atlas: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

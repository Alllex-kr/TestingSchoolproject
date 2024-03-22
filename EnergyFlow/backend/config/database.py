#from pymongo import MongoClient
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Alex:gruppe1@energyflow.tdhwiz9.mongodb.net/?retryWrites=true&w=majority&appName=EnergyFlow"

client = MongoClient(uri)

db = client.todo_db

collection_name = db["todo_collection"]
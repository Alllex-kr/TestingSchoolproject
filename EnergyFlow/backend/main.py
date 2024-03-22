from fastapi import FastAPI
from routes.route import router

app = FastAPI()


app.include_router(router)

# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://Alex:gruppe1@energyflow.tdhwiz9.mongodb.net/?retryWrites=true&w=majority&appName=EnergyFlow"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


#from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://Alex:gruppe1@energyflow.tdhwiz9.mongodb.net/?retryWrites=true&w=majority&appName=EnergyFlow"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)




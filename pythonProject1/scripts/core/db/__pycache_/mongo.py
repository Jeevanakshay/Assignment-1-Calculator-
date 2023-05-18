from pymongo import MongoClient
from config.config import mongo_db

client = MongoClient(mongo_db)
# Creating database
db = client.interns_b2_23
collection_grocery = db.jeevan




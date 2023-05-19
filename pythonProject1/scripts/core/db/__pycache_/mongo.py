from pymongo import MongoClient
from scripts.constants.app_constants import Mongo_db

client = MongoClient(Mongo_db.db_grocery)
# Creating database
db = client.interns_b2_23
collection_grocery = db.jeevan




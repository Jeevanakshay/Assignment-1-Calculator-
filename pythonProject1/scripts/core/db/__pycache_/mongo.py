from pymongo import MongoClient
from scripts.constants.app_configuration import URI

client = MongoClient(URI)
# Creating database
db = client.interns_b2_23
collection_grocery = db.jeevan






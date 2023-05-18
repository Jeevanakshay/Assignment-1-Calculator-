from pymongo import MongoClient  # import mongo client to connect

# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# Creating database
db = client.interns_b2_23
snacks_item = {"name": "ks",
               "quantity": "3",
               "price": "3",
               "tax_price": "3"
               }
# # Creating document
Snacks = db.jeevan_snacks_item
# # Inserting data
Snacks.insert_one(snacks_item)
# # Fetching data
print(Snacks.find_one({"product_id": "5678"}))

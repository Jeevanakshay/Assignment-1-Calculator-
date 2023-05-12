from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# Creating database
db = client.interns_b2_23
items_lists = db.jeevan


class snacks(BaseModel):
    name: str
    quantity: int
    price: int
    tax_price: float


product = {}
app = FastAPI()


@app.post("/models/{item_id}")
async def create_grocery(item_id: int, snacks_item: snacks):
    product[item_id] = (snacks_item.dict())
    if snacks_item.quantity:
        total_price = snacks_item.quantity * snacks_item.price
        items_lists.insert_one(snacks_item.dict())
        items_lists.insert_one({"Total_Price": total_price})
        return product


@app.get("/hello")
def get_total():
    items = (items_lists.find())
    new_list = []
    for item in items:
        del item["_id"]
        new_list.append(item)
    return new_list


@app.put("/welcome/{name}")
def update_item(name: str, update_items: snacks):
    items_lists.update_one({"name": name}, {"$set": update_items.dict()})
    return "updated"


@app.delete("/delete_snacks/{item_id}")
async def delete_item(item_id: str):
    items_lists.delete_one({"name": item_id})
    return "Deleted"

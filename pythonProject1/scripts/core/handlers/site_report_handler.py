from schema.models import Snacks
from scripts.core.db.__pycache_.mongo import collection_grocery
from scripts.core.db.__pycache_ import mongo
from scripts.constants.app_constants import Aggregation

collection = mongo.collection_grocery


def create_grocery( snacks_item: Snacks):
    """function is creates to get the input"""
    try:
        if not snacks_item.quantity:
            return "No quantity is listed "
        total_price = snacks_item.quantity * snacks_item.price
        collection_grocery .insert_one(snacks_item.dict())
        collection_grocery .insert_one({"Total_Price": total_price})
        return "Successfully"
    except Exception as e:
        return "Error", str(e)


def get_all_details():
    """"returns the values from data model"""
    items = (collection_grocery .find())
    new_list = []
    for item in items:
        del item["_id"]
        new_list.append(item)
    return new_list


def update_item(name: str, update_items: Snacks):
    """updating a list in put function"""
    """"name:str is a query , update_item:Snacks is filter"""
    try:
        results = collection_grocery .update_one({"name_update": name}, {"$set": update_items.dict()})
        if results.modified_count > 0:
            return "updated"
        else:
            return "Not updated"
    except Exception as e:
        return "Error", str(e)


def delete_item(item_id: str):
    """Delete the particular list"""
    try:
        collection_grocery .delete_one({"delete_name": item_id})
        return "Deleted"
    except Exception as e:
        return "Error", str(e)


def pipeline():
    data = collection.aggregate(Aggregation.agg)
    print(data)
    total = list(data)[0]['total']
    return {'Total_price': total}

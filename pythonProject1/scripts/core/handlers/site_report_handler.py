from schema.models import Snacks
from scripts.core.db.__pycache_.mongo import collection_grocery
from scripts.core.db.__pycache_ import mongo
from scripts.constants.app_constants import Aggregation
from scripts.logging.logger import logger
from scripts.constants.app_constants import comments, statement
from scripts.Execption.execption import BillingHandlerException

collection = mongo.collection_grocery


class Grocery:

    def create_grocery(self, snacks_item: Snacks):
        """function is creates to get the input"""
        try:
            if not snacks_item.quantity:
                logger.warning("Warming:No quantity is in listed ")
                return statement.Create
            total_price = snacks_item.quantity * snacks_item.price
            collection_grocery.insert_one(snacks_item.dict())
            # collection_grocery.insert_one({comments.total_price: total_price})
            logger.info("Info:Successfully items are inserted in database ")
            return statement.create_successfully
        except Exception as e:
            logger.error(BillingHandlerException.EX001.format(error=str(e)))

    def get_all_details(self):
        """"returns the values from data model"""

        items = (collection_grocery.find())
        new_list = []
        for item in items:
            del item["_id"]
            new_list.append(item)
        logger.info("Info:All the information is present in the database")
        return new_list

    def update_item(self, name: str, update_items: Snacks):
        """updating a list in put function"""
        """"name:str is a query , update_item:Snacks is filter"""
        try:
            results = collection_grocery.update_one({comments.name: name}, {comments.list: update_items.dict()})
            if results.modified_count > 0:
                logger.info("Info:Items are updated in the bill")
                return statement.update
            else:
                logger.warning("warning:Issues in updation in bill")
                return statement.update_if_not
        except Exception as e:
            logger.error(BillingHandlerException.EX003.format(error=str(e)))

    def delete_item(self, item_id: str):
        """Delete the particular list"""
        try:
            collection_grocery.delete_one({"name": item_id})
            logger.info("Info:Particular item is deleted in bill")
            return statement.delete
        except Exception as e:
            logger.error(BillingHandlerException.EX004.format(error=str(e)))

    def pipeline(self):
        """
        Email will be sent to the particular user
        :return:
        """
        try:
            data = collection.aggregate(Aggregation.agg)
            print(data)
            total = list(data)[0][comments.total_cost]
            logger.info("Email is sent successfully")
            return total
        except Exception as e:
            logger.error(BillingHandlerException.EX005.format(error=str(e)))


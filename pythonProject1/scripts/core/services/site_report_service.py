"""Calling all the function to execute the output"""
from scripts.core.handlers.email_handlers import send_email, Email
from scripts.core.handlers.site_report_handler import Grocery
from schema.models import Snacks
from fastapi import APIRouter
from scripts.constants.app_constants import api_obj
from json2html import *
from scripts.logging.logger import logger
from scripts.Execption.execption import ServiceException

app = APIRouter()
grocery_obj = Grocery()


@app.post(api_obj.Create_Post)
def fun(snacks_item: Snacks):
    """
    :param snacks_item:
    :return:
    """
    final_json = {"status": False, "message": None}
    try:
        response = grocery_obj.create_grocery(snacks_item)
        final_json["status"] = True
        final_json["message"] = response
    except Exception as err:
        logger.error(str(err))
    return final_json


@app.get(api_obj.Displaying_Get)
def fun():
    """
    :return: displaying entire data which is stored in database
    """
    try:
        return grocery_obj.get_all_details()
    except Exception as err:
        logger.error(str(err))


@app.put(api_obj.Updating_Grocery)
def fun(name: str, update_items: Snacks):
    """
    :param name:
    :param update_items:
    :return:
    """
    final_json = {"status": False, "message": None}
    try:
        response = grocery_obj.update_item(name, update_items)
        final_json["status"] = True
        final_json["message"] = response
    except Exception as err:
        logger.error(str(err))
    return final_json


@app.delete(api_obj.Delete_Grocery)
async def fun(item_id: str):
    """
    :param item_id:
    :return:
    """
    final_json = {"status": False, "message": None}
    try:
        response = grocery_obj.delete_item(item_id)
        final_json["status"] = True
        final_json["message"] = response
    except Exception as err:
        logger.error(str(err))
    return final_json


@app.post(api_obj.Email)
def fun(email: Email):
    """
    :param email:
    :return:
    """
    try:
        all_billing_list_json = grocery_obj.get_all_details()
        billing_table = json2html.convert(json=all_billing_list_json)
        total_value = grocery_obj.pipeline()
        message = f"Table : {billing_table} \n total value : {total_value}"
        return send_email(message, email)
    except Exception as e:
        logger.error(ServiceException.EX007.fromat(error=e))


@app.get(api_obj.Pipeline)
def func():
    """
    :return:
    """
    try:
        return grocery_obj.pipeline()
    except Exception as err:
        logger.error(str(err))
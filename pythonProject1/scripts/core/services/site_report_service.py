from scripts.core.handlers.email_handlers import send_email, Email
from scripts.core.handlers.site_report_handler import create_grocery, get_all_details, update_item, delete_item,pipeline
from schema.models import Snacks
from fastapi import APIRouter
from scripts.constants.app_constants import api_obj

app = APIRouter()


@app.post(api_obj.Create_Post)
def fun(snacks_item: Snacks):
    return create_grocery(snacks_item)


@app.get(api_obj.Displaying_Get)
def fun():
    return get_all_details()


@app.put(api_obj.Updating_Grocery)
def fun(name: str, update_items: Snacks):
    return update_item(name, update_items)


@app.delete(api_obj.Delete_Grocery)
async def fun(item_id: str):
    return delete_item(item_id)


@app.post(api_obj.Email)
def fun(email: Email):
    total_value = pipeline()
    return send_email(str(total_value), email)


@app.get(api_obj.Pipeline)
def func():
    return pipeline()

from scripts.core.handlers.email_handlers import send_email, Email
from scripts.core.handlers.site_report_handler import create_grocery, get_all_details, update_item, delete_item,pipeline
from schema.models import Snacks
from fastapi import APIRouter

app = APIRouter()


@app.post("/models/{item_id}")
def fun(snacks_item: Snacks):
    return create_grocery(snacks_item)


@app.get("/return")
def fun():
    return get_all_details()


@app.put("/updating_items/{name}")
def fun(name: str, update_items: Snacks):
    return update_item(name, update_items)


@app.delete("/delete_snacks/{item_id}")
async def fun(item_id: str):
    return delete_item(item_id)


@app.post("/Email")
def fun(email: Email):
    total_value = pipeline()
    return send_email(str(total_value), email)


@app.get("/total_sum")
def func():
    return pipeline()

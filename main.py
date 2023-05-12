from fastapi import FastAPI
from schema.models import Snacks
from scripts.core.handlers.site_report_handler import create_grocery, get_total, update_item, delete_item

app = FastAPI()


@app.post("/models/{item_id}")
def fun(item_id: int, snacks_item: Snacks):
    return create_grocery(item_id, snacks_item)


@app.get("/hello")
def fun():
    return get_total


@app.put("/welcome/{name}")
def fun(name: str, update_items: Snacks):
    return update_item(name, update_items)


@app.delete("/delete_snacks/{item_id}")
async def fun(item_id: str):
    return delete_item(item_id)

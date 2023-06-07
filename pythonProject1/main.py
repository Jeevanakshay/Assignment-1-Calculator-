from fastapi import FastAPI
import uvicorn
from scripts.core.services.site_report_service import app as grocery_router
from scripts.constants.app_configuration import *

app_main = FastAPI()

app_main.include_router(grocery_router)

if __name__ == "__main__":
    uvicorn.run("main:app_main", host=SERVICE_HOST, port=int(SERVICE_PORT), reload=True)

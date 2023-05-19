from fastapi import FastAPI
import uvicorn
from scripts.core.services.site_report_service import app as grocery_router

app_main = FastAPI()

app_main.include_router(grocery_router)

if __name__ == "__main__":
    uvicorn.run("main:app_main", reload=True)


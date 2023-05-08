from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Happy All !!"}, {"Name": "JeevanAkshay"}, {"Age": 21}

@app.get("/details")
def tree():
    return {"College": "PEC"}, {"Degree": "B.E"}

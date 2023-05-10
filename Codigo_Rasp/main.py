from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

MAX = 100

@app.get("/get_percentages")
def get_percentages() -> dict[str, list[int]]:
    fake = {
        "percentages": [69, 33, 47]
    }

    return fake

@app.get("/start")
def start(liquid1: int, liquid2: int, liquid3: int): 
    pass
import json
from funcs import get_coor, get_human
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root():
    return{"Made By": "BelitK"}


@app.get("/vision")
async def boxes_and_confidence(request: Request):
    """Object detection using YOLO"""
    a = await request.json()
    image = json.loads(a)["b64"]
    threshold = json.loads(a)["threshold"]
    return get_coor(image, threshold)


@app.get("/human")
async def human_detection(request: Request):
    """Human detection using Hog-SVM"""
    a = await request.json()
    image = json.loads(a)["b64"]
    return get_human(image)

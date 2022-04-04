from fastapi import FastAPI, Request
import json
from funcs import get_coor
app = FastAPI()

@app.get("/")
def read_root():
        return{"Hello":"world"}
@app.get("/test")
async def return_test(request: Request):
        a= await request.json()
        image = json.loads(a)["b64"]
        return get_coor(image,threshold=0.3)
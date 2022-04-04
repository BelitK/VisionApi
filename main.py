from fastapi import FastAPI, Request
import json
app = FastAPI()

@app.get("/")
def read_root():
        return{"Hello":"world"}
@app.get("/test")
async def return_test(request: Request):
        a= await request.json()
        print(a["b64"])
        return a["test"]
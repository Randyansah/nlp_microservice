import transformer
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI 
from lib.hug_me import main as hg
from pydantic import BaseModel

app=FastAPI()
class Hug_me(BaseModel):
    name:str

@app.post("/Hug_me")    
async def nlp(hug_me:Hug_me):
    result=hg(name=Hug_me.name)
    payload={"Natural Language page":result}
    json_compatible_item_data=jsonable_encoder(payload)

@app.get("/")
async def root():
    return {"nlp":"Hello functions"}

@app.get("/real_d/{input1}/{input2}")
async def real_d(input1:int,input2:str):
    return{"Action":hg(input1,input2)}


    

       
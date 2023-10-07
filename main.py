import transformers
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI 
from lib.hug_me import nlp
from pydantic import BaseModel
import tensorflow


app=FastAPI()
class Natural_language(BaseModel):
    number: int
    text: str

@app.get("/")
def index():
    return {"message":"Hello World"}

    
@app.post("/Hugging_face")
async def natural_lang(input_data:Natural_language):
    text=input_data.text
    number=input_data.number
    return{"NLP":nlp(number,text)}

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8080)       
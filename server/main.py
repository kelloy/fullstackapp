from fastapi import FastAPI
from service import predict
from classes import classes

app = FastAPI()

@app.post("/api/prediction")
async def predictionsoutput(input_string: classes.input):
    predictions = predict.predictions(input_string.input)
    return predictions
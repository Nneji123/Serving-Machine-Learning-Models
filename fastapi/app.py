# 1. Library imports
import pandas as pd
import joblib
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from models import *
import numpy as np

# 2. Create the app object
app = FastAPI(
    title="Car Price Prediction API",
    description="""An API that utilises a Machine Learning model to predict the price of a given car make and model based on various features.""",
    version="0.0.1",
    debug=True,
)


@app.get("/", response_class=PlainTextResponse)
async def running():
    note = """
Car Price Prediction API 🙌🏻
Note: add "/docs" to the URL to get the Swagger UI Docs or "/redoc"
  """
    return note


favicon_path = "favicon.png"


@app.get("/favicon.png", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@app.post("/predict")
def predict(data: CarPrediction):

    features = np.array(
        [
            [
                data.enginesize,
                data.curbweight,
                data.horsepower,
                data.highwaympg,
                data.carwidth,
                data.wheelbase,
                data.drivewheel,
                data.citympg,
                data.boreratio,
                data.cylindernumber
            ]
        ]
    )

    model = joblib.load("./models/sklearn_gbr.pkl")

    predictions = model.predict(features)
    value = str(predictions)[1:-1]
    #return {f"The price of your car is {value}$"}
    return {value}
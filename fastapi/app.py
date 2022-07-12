# 1. Library imports
import pandas as pd
import joblib
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from models import *
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

# 2. Create the app object
app = FastAPI()


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
                data.symboling,
                data.fueltype,
                data.aspiration,
                data.doornumber,
                data.carbody,
                data.drivewheel,
                data.enginelocation,
                data.wheelbase,
                data.carlength,
                data.carwidth,
                data.carheight,
                data.curbweight,
                data.enginetype,
                data.cylindernumber,
                data.enginesize,
                data.fuelsystem,
                data.boreratio,
                data.stroke,
                data.compressionratio,
                data.horsepower,
                data.peakrpm,
                data.citympg,
                data.highwaympg,
            ]
        ]
    )

    model = joblib.load("./models/sklearn_gbr.pkl")

    predictions = model.predict(features)
    value = str(predictions)[1:-1]
    return {f"The price of your car is {value}$"}

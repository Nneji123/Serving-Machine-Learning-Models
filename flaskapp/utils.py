import joblib
import numpy as np


def predict_price(
    symboling,
    fueltype,
    aspiration,
    doornumber,
    carbody,
    drivewheel,
    enginelocation,
    wheelbase,
    carlength,
    carwidth,
    carheight,
    curbweight,
    enginetype,
    cylindernumber,
    enginesize,
    fuelsystem,
    boreratio,
    stroke,
    compressionratio,
    horsepower,
    peakrpm,
    citympg,
    highwaympg,
):

    data = np.array(
        [
            [
                symboling,
                fueltype,
                aspiration,
                doornumber,
                carbody,
                drivewheel,
                enginelocation,
                wheelbase,
                carlength,
                carwidth,
                carheight,
                curbweight,
                enginetype,
                cylindernumber,
                enginesize,
                fuelsystem,
                boreratio,
                stroke,
                compressionratio,
                horsepower,
                peakrpm,
                citympg,
                highwaympg,
            ]
        ]
    )

    model = joblib.load("./models/sklearn_gbr.pkl")
    predictions = model.predict(data)

    return predictions

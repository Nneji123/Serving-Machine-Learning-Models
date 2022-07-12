from pydantic import BaseModel


class CarPrediction(BaseModel):
    symboling: int
    fueltype: int
    aspiration: float
    doornumber: float
    carbody: float
    drivewheel: float
    enginelocation: float
    wheelbase: float
    carlength: int
    carwidth: int
    carheight: float
    curbweight: float
    enginetype: float
    cylindernumber: float
    enginesize: float
    fuelsystem: float
    boreratio: int
    stroke: int
    compressionratio: float
    horsepower: float
    peakrpm: float
    citympg: float
    highwaympg: float

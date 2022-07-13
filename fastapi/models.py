from pydantic import BaseModel


class CarPrediction(BaseModel):

    enginesize: float
    curbweight: float
    horsepower: float
    highwaympg: float
    carwidth: float
    wheelbase: float
    drivewheel: float
    citympg: float
    boreratio: float
    cylindernumber: float

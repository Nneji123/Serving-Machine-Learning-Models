import bentoml
import bentoml.sklearn
from bentoml.io import NumpyNdarray, PandasDataFrame

import pickle
import numpy as np
import pandas as pd

# Load processors 

predictor = bentoml.sklearn.load_runner("gbr:latest")

service = bentoml.Service(
    "gbr", runners=[predictor]
)

# Create an API function
@service.api(input=PandasDataFrame(), output=NumpyNdarray())
def predict(df: pd.DataFrame) -> np.ndarray:

   # Process data
    df = pd.read_csv("./Data/cars.csv", usecols=["symboling",
        "fueltype",
        "aspiration",
        "doornumber",
        "carbody",
        "drivewheel",
        "enginelocation",
        "wheelbase",
        "carlength",
        "carwidth",
        "carheight",
        "curbweight",
        "enginetype",
        "cylindernumber",
        "enginesize",
        "fuelsystem",
        "boreratio",
        "stroke",
        "compressionratio",
        "horsepower",
        "peakrpm",
        "citympg",
        "highwaympg",
        "price"])
    data = pd.DataFrame(df)
    # scaled_df = pd.DataFrame([scaler.run(df)], columns=df.columns)
    # processed = pd.DataFrame(
    #     [pca.run(scaled_df)], columns=["col1", "col2", "col3"]
    # )

    # Predict
    result = predictor.run(data)
    return np.array(result)

    # use the command : bentoml serve service.py:service --reload to load the swagger ui docs
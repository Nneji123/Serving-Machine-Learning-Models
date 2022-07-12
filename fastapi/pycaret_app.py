# 1. Library imports
import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI

# 2. Create the app object
app = FastAPI()

# . Load trained Pipeline
model = load_model("./model")

# Define predict function


@app.post("/predict")
def predict(carat_weight, cut, color, clarity, polish, symmetry, report):
    data = pd.DataFrame([[carat_weight, cut, color, clarity, polish, symmetry, report]])
    data.columns = [
        "Carat Weight",
        "Cut",
        "Color",
        "Clarity",
        "Polish",
        "Symmetry",
        "Report",
    ]

    predictions = predict_model(model, data=data)
    return {"price": int(predictions["Label"][0])}

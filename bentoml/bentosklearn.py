import bentoml
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

dataset = pd.read_csv(
    "./Data/cars.csv",
        usecols=["enginesize",
        "curbweight",
        "horsepower",
        "highwaympg",
        "carwidth",
        "wheelbase",
        "drivewheel",
        "citympg",
        "boreratio",
        "cylindernumber",
        "price"]
)

# get all categorical columns in the dataframe


from sklearn.preprocessing import LabelEncoder


def encode(data):
    catCols = [col for col in data.columns if data[col].dtype == "O"]
    lb_make = LabelEncoder()

    for item in catCols:
        data[item] = lb_make.fit_transform(data[item])

    return data


df = encode(dataset)

X = df.drop("price", axis=1)
y = df.price

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

model = GradientBoostingRegressor()

model.fit(X_train, y_train)

#bentoml.sklearn.save("scaler", scaler)
bentoml.sklearn.save("gbr", model)

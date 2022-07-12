import bentoml
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('./Data/cars.csv', usecols=['symboling', 'fueltype', 'aspiration',
       'doornumber', 'carbody', 'drivewheel', 'enginelocation', 'wheelbase',
       'carlength', 'carwidth', 'carheight', 'curbweight', 'enginetype',
       'cylindernumber', 'enginesize', 'fuelsystem', 'boreratio', 'stroke',
       'compressionratio', 'horsepower', 'peakrpm', 'citympg', 'highwaympg',
       'price'])

# get all categorical columns in the dataframe


from sklearn.preprocessing import LabelEncoder
def encode(data):
    catCols = [col for col in data.columns if data[col].dtype=="O"]
    lb_make = LabelEncoder()

    for item in catCols:
        data[item] = lb_make.fit_transform(data[item])

    return data

df = encode(dataset)

X = df.drop('price', axis=1)
y = df.price
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
model = GradientBoostingRegressor().fit(X_train, y_train)

x = model.predict(X_test)
from sklearn.metrics import r2_score
score = print(r2_score(x, y_test))

# # `save` a given classifier and retrieve coresponding tag:
# tag = bentoml.sklearn.save_model('gbr', model)

# # retrieve metadata with `bentoml.models.get`:
# metadata = bentoml.models.get(tag)

# # load the model back:
# loaded = bentoml.sklearn.load_model("gbr:latest")

# # Run a given model under `Runner` abstraction with `to_runner`
# runner = bentoml.sklearn.get(tag).to_runner()
# runner.init_local()
# runner.run([[1,2,3,4,5]])
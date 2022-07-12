import bentoml
import pandas as pd

from pycaret.datasets import get_data
from pycaret.regression import setup as pycaret_setup
from pycaret.regression import save_model
from pycaret.regression import tune_model
from pycaret.regression import create_model
from pycaret.regression import predict_model
from pycaret.regression import finalize_model

dataset = pd.read_csv("./Data/cars.csv")
data = dataset.sample(frac=0.95, random_state=786)
data_unseen = dataset.drop(data.index)
data.reset_index(inplace=True, drop=True)
data_unseen.reset_index(inplace=True, drop=True)

pycaret_setup(data=data, target="price", session_id=123, silent=True)
gbr = create_model('gbr')
tuned_gbr = tune_model(gbr)
final_dt = finalize_model(tuned_gbr)

# `save` a given classifier and retrieve coresponding tag:
tag = bentoml.pycaret.save("reg", final_dt)

# retrieve metadata with `bentoml.models.get`:
metadata = bentoml.models.get(tag)

# `load` the model back in memory:
model = bentoml.pycaret.load("reg:latest")

# Run a given model under `Runner` abstraction with `load_runner`
input_data = pd.from_csv("./Data/cars.csv")
runner = bentoml.pycaret.load_runner(tag)
runner.run(pd.DataFrame("./Data/cars.csv"))




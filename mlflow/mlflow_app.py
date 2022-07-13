import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder

#tell mlflow to start logging
with mlflow.start_run():

    #read in the data using pandas
    data = pd.read_csv('./data/cars.csv')

    ## Log data to mlflow
    mlflow.log_artifact('./data/cars.csv')

    #print data shape
    print(f'data shape is: {data.shape}')

    #check data has been read in properly
    def encode(data):
        catCols = [col for col in data.columns if data[col].dtype == "O"]
        lb_make = LabelEncoder()

        for item in catCols:
            data[item] = lb_make.fit_transform(data[item])
        
        return data

    df = encode(data)

    print(df.head())

    #create a dataframe with all training data except the target column
    X = df.drop(columns=['price'])

    #check that the target variable has been removed
    print('check that the target variable has been removed')
    print(X.head())
    print(X.shape)

    #separate target values
    y = df.price

    #view target values
    print(f'first 5 target values are: {y[0:5]}')

    #split dataset into train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1)

    model = GradientBoostingRegressor()

    model.fit(X_train, y_train)   


    #log n_neighbors param to mlflow
    mlflow.log_param('gbr', model)

    print(f'GBR model is training - gbr: {model}')

    #show first 5 model predictions on the test data
    preds = model.predict(X_test)

    #check accuracy of our model on the test data
    from sklearn.metrics import r2_score
    accuracy = r2_score(preds, y_test)

    #log model accuracy to mlflow
    mlflow.log_metric('R2_Score', accuracy)

    print(f'model accuracy is: {accuracy*100}%')

    # Logging model to MLFlow
    mlflow.sklearn.log_model(model, 'model')

    # to view the tracking page run 'mlflow ui'
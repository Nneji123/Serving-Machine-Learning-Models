import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import sys

#tell mlflow to start logging
with mlflow.start_run():

    #read in the data using pandas
    df = pd.read_csv('data/diabetes_data.csv')

    ## Log data to mlflow
    mlflow.log_artifact('data/diabetes_data.csv')

    #print data shape
    print(f'data shape is: {df.shape}')

    #check data has been read in properly
    print(df.head())

    #create a dataframe with all training data except the target column
    X = df.drop(columns=['diabetes'])

    #check that the target variable has been removed
    print('check that the target variable has been removed')
    print(X.head())
    print(X.shape)

    #separate target values
    y = df['diabetes'].values

    #view target values
    print(f'first 5 target values are: {y[0:5]}')

    #split dataset into train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1, stratify=y)

    #knn model parameter
    n_neighbors = int(sys.argv[1]) if len(sys.argv) > 1 else 5

    #log n_neighbors param to mlflow
    mlflow.log_param('n_neighbors', n_neighbors)

    # Create KNN classifier
    knn = KNeighborsClassifier(n_neighbors = n_neighbors)

    # Fit the classifier to the data
    knn.fit(X_train,y_train)

    print(f'knn model is training - n_neigbors: {n_neighbors}')

    #show first 5 model predictions on the test data
    knn.predict(X_test)[0:5]

    #check accuracy of our model on the test data
    accuracy = knn.score(X_test, y_test)

    #log model accuracy to mlflow
    mlflow.log_metric('accuracy', accuracy)

    print(f'model accuracy is: {accuracy}')
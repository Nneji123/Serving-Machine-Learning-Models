<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

  - [About :boom:](#about-boom)
    - [Table of Contents :book:](#table-of-contents-book)
  - [Repository Structure](#repository-structure)
  - [Getting Started](#getting-started)
    - [Configuring Python Environment](#configuring-python-environment)
    - [Installing Dependencies](#installing-dependencies)
  - [Building Machine Learning Model: Car Price Prediction](#building-machine-learning-model-car-price-prediction)
    - [How to save Models with Joblib](#how-to-save-models-with-joblib)
    - [Version Control your models with DVC(Data Version Control)](#version-control-your-models-with-dvcdata-version-control)
  - [Creating Applications with your Model :computer:](#creating-applications-with-your-model-computer)
    - [Serving Models with FastAPI](#serving-models-with-fastapi)
    - [Serving Models with Flask](#serving-models-with-flask)
    - [Serving Models with BentoML](#serving-models-with-bentoml)
    - [Serving Models with Mlflow](#serving-models-with-mlflow)
    - [Serving Models with Streamlit](#serving-models-with-streamlit)
    - [Serving Models as Desktop/ Android Applications](#serving-models-as-desktop-android-applications)
  - [How to Test your models and applications with Pytest](#how-to-test-your-models-and-applications-with-pytest)
  - [Deploying your applications to AWS and Heroku](#deploying-your-applications-to-aws-and-heroku)
    - [Working with Dockerfiles](#working-with-dockerfiles)
  - [Github Actions](#github-actions)
    - [Using Github Actions and Heroku for CI/CD](#using-github-actions-and-heroku-for-cicd)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Serving Machine Learning Models :robot:


## About :boom:
**This repository contains instructions, template source code and examples on how to serve/deploy machine learning models using various frameworks and applications such as Docker, Flask, FastAPI, BentoML, Streamlit, MLflow and even code on how to deploy your machine learning model as an android app.** 

**The Repository also has code and how-to's for deploying your apps to various cloud platforms(AWS, Heroku, Vercel etc), working with Github actions for CI/CD(Continuous Integration and Continuous Development), TDD(Test driven development) with pytest and other useful information.**

### Table of Contents :book:


## Repository Structure
Generate repo structure with 'tree' command in linux. generate toc  npm install --save markdown-toc, and markdown-toc
```bash
.
├── androidapp
│   ├── buildozer.spec
│   ├── data
│   │   └── icon.png
│   ├── main.py
│   └── requirements.txt
├── bentoml
│   ├── bentofile.yaml
│   ├── bentosklearn.py
│   ├── Data
│   │   ├── cars.csv
│   │   ├── cars.zip
│   │   └── Data Dictionary - carprices.xlsx
│   ├── __init__.py
│   ├── requirements.txt
│   └── service.py
├── Data
│   ├── cars.csv
│   ├── cars.zip
│   └── Data Dictionary - carprices.xlsx
├── fastapi
│   ├── app.py
│   ├── Dockerfile
│   ├── favicon.png
│   ├── heroku.yml
│   ├── models
│   │   ├── model.pkl
│   │   └── sklearn_gbr.pkl
│   ├── models.py
│   ├── requirements.txt
│   └── train.py
├── flaskapp
│   ├── app.py
│   ├── models
│   │   ├── model.pkl
│   │   └── sklearn_gbr.pkl
│   ├── Procfile
│   ├── requirements.txt
│   ├── runtime.txt
│   ├── static
│   │   ├── bootstrap.css
│   │   ├── bootstrap.css.map
│   │   ├── bootstrap-grid.css
│   │   ├── bootstrap-grid.css.map
│   │   ├── bootstrap-grid.min.css
│   │   ├── bootstrap-grid.min.css.map
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap.min.css.map
│   │   ├── bootstrap-reboot.css
│   │   ├── bootstrap-reboot.css.map
│   │   ├── bootstrap-reboot.min.css
│   │   ├── bootstrap-reboot.min.css.map
│   │   ├── favicon.png
│   │   └── w3.css
│   ├── templates
│   │   ├── index.html
│   │   ├── result.html
│   │   ├── static
│   │   │   ├── bootstrap.css
│   │   │   ├── bootstrap.css.map
│   │   │   ├── bootstrap-grid.css
│   │   │   ├── bootstrap-grid.css.map
│   │   │   ├── bootstrap-grid.min.css
│   │   │   ├── bootstrap-grid.min.css.map
│   │   │   ├── bootstrap.min.css
│   │   │   ├── bootstrap.min.css.map
│   │   │   ├── bootstrap-reboot.css
│   │   │   ├── bootstrap-reboot.css.map
│   │   │   ├── bootstrap-reboot.min.css
│   │   │   ├── bootstrap-reboot.min.css.map
│   │   │   ├── favicon.png
│   │   │   └── w3.css
│   │   └── w3.css
│   └── utils.py
├── __init__.py
├── LICENSE.md
├── mlflow
│   ├── data
│   │   ├── cars.csv
│   │   ├── cars.zip
│   │   └── Data Dictionary - carprices.xlsx
│   ├── mlflow_app.py
│   ├── mlruns
│   │   └── 0
│   │       ├── 387be03e078049f69b2f68c916b1c4fa
│   │       │   ├── meta.yaml
│   │       │   └── tags
│   │       │       ├── mlflow.source.git.commit
│   │       │       ├── mlflow.source.name
│   │       │       ├── mlflow.source.type
│   │       │       └── mlflow.user
│   │       ├── 7813850eea9344c0a8e67670fd1eb52b
│   │       │   ├── artifacts
│   │       │   │   └── cars.csv
│   │       │   ├── meta.yaml
│   │       │   └── tags
│   │       │       ├── mlflow.source.git.commit
│   │       │       ├── mlflow.source.name
│   │       │       ├── mlflow.source.type
│   │       │       └── mlflow.user
│   │       ├── 8d81478e0b7a4ab78a76afb2c0225d85
│   │       │   ├── meta.yaml
│   │       │   └── tags
│   │       │       ├── mlflow.source.git.commit
│   │       │       ├── mlflow.source.name
│   │       │       ├── mlflow.source.type
│   │       │       └── mlflow.user
│   │       ├── d152c4ed8ff846459df57701db6542b0
│   │       │   ├── artifacts
│   │       │   │   └── cars.csv
│   │       │   ├── meta.yaml
│   │       │   ├── metrics
│   │       │   │   └── R2_Score
│   │       │   ├── params
│   │       │   │   └── gbr
│   │       │   └── tags
│   │       │       ├── mlflow.source.git.commit
│   │       │       ├── mlflow.source.name
│   │       │       ├── mlflow.source.type
│   │       │       └── mlflow.user
│   │       ├── ee11d66e35c64736bda4bd41429a678b
│   │       │   ├── artifacts
│   │       │   │   └── cars.csv
│   │       │   ├── meta.yaml
│   │       │   └── tags
│   │       │       ├── mlflow.source.git.commit
│   │       │       ├── mlflow.source.name
│   │       │       ├── mlflow.source.type
│   │       │       └── mlflow.user
│   │       ├── f6aeeb22a768414e81e1825e8b65c728
│   │       │   ├── artifacts
│   │       │   │   ├── cars.csv
│   │       │   │   └── model
│   │       │   │       ├── conda.yaml
│   │       │   │       ├── MLmodel
│   │       │   │       ├── model.pkl
│   │       │   │       ├── python_env.yaml
│   │       │   │       └── requirements.txt
│   │       │   ├── meta.yaml
│   │       │   ├── metrics
│   │       │   │   └── R2_Score
│   │       │   ├── params
│   │       │   │   └── gbr
│   │       │   └── tags
│   │       │       ├── mlflow.log-model.history
│   │       │       ├── mlflow.source.git.commit
│   │       │       ├── mlflow.source.name
│   │       │       ├── mlflow.source.type
│   │       │       └── mlflow.user
│   │       ├── meta.yaml
│   │       └── tags
│   │           └── mlflow.note.content
│   └── requirements.txt
├── models
│   ├── model.pkl
│   └── sklearn_gbr.pkl
├── Notebooks
│   ├── Car_Price_Prediction_with_Pycaret.ipynb
│   └── Kivy_App_To_APK.ipynb
├── README.md
├── requirements.txt
├── setup.sh
├── streamlitapp
│   └── streamlit_app.py
├── tests
│   └── test_api.py
├── todo.txt
└── vercel.json
```

## Getting Started
Before we get into building and deploying our models we'll have to setup our environment. I use 'pyenv' for managing different versions of python and pyenv-virtualenv for setting up virtual environments. You can learn how to install pyenv on your operating system by checking out their official [github](https://github.com/pyenv/pyenv). Also it's important you have git installed on your system so you can easily clone this repository. If you're on Linux you can install git by running this command:
```
sudo apt-get install git
```
### Configuring Python Environment
To easily setup our environment I've created a shell script named **'setup.sh'** for easily installing and configuring pyenv on your system. It's assumed we are working with Linux but there are ways to install pyenv on windows too. To install pyenv easily with the shell script run the following commands in your terminal:
1. Clone this repository:
```bash
git clone https://github.com/Nneji123/Serving-Machine-Learning-Models.git
```
2. Change the working directory
```bash
cd Serving-Machine-Learning-Models
```
3. Run the script
```
./setup.sh
```
4. After running the script you can check if pyenv successfully installed by running:
```
pyenv versions
```
And you should see Python 3.8.10 as the installed version.
### Installing Dependencies and Creating virtual environments with pyenv
We will be working with python and some frameworks such as FastAPI, Flask, Streamlit etc and we will need to install their various dependencies. In each folder I've created specific **requirements.txt** files for installing the dependencies needed for each project. For example you can install the **FastAPI** application requirements with pip by running:
```bash
cd fastapi

pip install -r requirement.txt
```
Same goes for the other projects in this repository as well.
## Building Machine Learning Model: Car Price Prediction
In this project we will be building a machine learning regression model that can predict the price of a car based on some features. The dataset used can be found on [Kaggle]() and can also be found in this [repository](https://github.com/Nneji123/Serving-Machine-Learning-Models/blob/master/Data/cars.csv). You can check out the notebooks [folder](https://github.com/Nneji123/Serving-Machine-Learning-Models/tree/master/Notebooks) which contains the notebook used for analysing and visualising the data and building our model.
### How to save Models with Joblib
Joblib is a set of tools to provide lightweight pipelining in Python. You can read more about Joblib [here](https://joblib.readthedocs.io/en/latest/). To save our model I used joblib to save the model as a pickle file(.pkl) so we can later use the model to make predictions. To save your models(assuming you've built a model) you can do that by running:
```python
import joblib
model = LinearRegression
model.fit(X_train, y_train)
joblib.dump('model.pkl', model)
```
### Version Control your models with DVC(Data Version Control)
What is DVC for?
Data Version Control, or DVC, is a data and ML experiment management tool that takes advantage of the existing engineering toolset that we are familiar with (Git, CI/CD, etc.). DVC is meant to be run alongside Git. The git and DVC commands will often be used in tandem, one after the other. In this project I used DVC to manage our models and data. You can read more about DVC and how to use it [here](https://medium.com/towards-data-science/introduction-to-dvc-data-version-control-tool-for-machine-learning-projects-7cb49c229fe0). 

## Creating Applications with your Model :computer:
In this section we will be serving our models as applications using these frameworks:
1. FastAPI
2. Flask
3. BentoML
4. Mlflow
5. Streamlit
6. KivyMD

### Serving Models with FastAPI
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features are:

- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the - fastest Python frameworks available.

- Fast to code: Increase the speed to develop features by about 200% to 300%. *

- Fewer bugs: Reduce about 40% of human (developer) induced errors. *
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- Robust: Get production-ready code. With automatic interactive documentation.
- Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema. 

In this [tutorial](https://medium.com/towards-data-science/deploying-an-ml-model-with-fastapi-a-succinct-guide-69eceda27b21) you can learn how to serve your model as a RESTful API with FastAPI.
### Serving Models with Flask
### Serving Models with BentoML
### Serving Models with Mlflow
### Serving Models with Streamlit
### Serving Models as Desktop/ Android Applications

## How to Test your models and applications with Pytest
## Deploying your applications to AWS and Heroku
### Working with Dockerfiles
## Github Actions
### Using Github Actions and Heroku for CI/CD 


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
### Configuring Python Environment
### Installing Dependencies

## Building Machine Learning Model: Car Price Prediction
### How to save Models with Joblib
### Version Control your models with DVC(Data Version Control)

## Creating Applications with your Model :computer:
### Serving Models with FastAPI
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


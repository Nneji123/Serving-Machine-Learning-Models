import streamlit as st
import json
import requests as re

st.title("Car Price Prediction Web App")

# st.image("image.png")

st.write("""
## About

**This Streamlit App utilizes a Machine Learning model served as an API to predict the price of a car based on certain features.** 

""")


st.sidebar.header('Input Car Details')

names = st.sidebar.text_input("""Name of Car""")
enginesize = st.sidebar.number_input("""Input Engine Size""")
horsepower = st.sidebar.number_input("""Input Horse Power""")
highwaympg= st.sidebar.number_input("""Input Highway Miles Per Gallon""")
carwidth = st.sidebar.number_input("""Input Car Width""")
wheelbase = st.sidebar.number_input("""Input Wheel Base""")
drivewheel = st.sidebar.number_input("""Input Drive Wheel""")
citympg = st.sidebar.number_input("""Input City Miles Per Gallon""")
boreratio = st.sidebar.number_input("""Input Bore Ratio""")
cylindernumber = st.sidebar.number_input("""Input Cylinder Number""")

    



if st.button("Predict Price"):
    values = {
            "enginesize": enginesize,
            "curbweight": curbweight,
            "horsepower": horsepower,
            "highwaympg": highwaympg,
            "carwidth": carwidth,
            "wheelbase": wheelbase,
            "drivewheel": drivewheel,
            "citympg": citympg,
            "boreratio": boreratio,
            "cylindernumber": cylindernumber
        }



    res = re.post(f"https://carpriceapi.herokuapp.com/predict",json=values)
    json_str = json.dumps(res.json())
    resp = json.loads(json_str)
    
    if names=='':
        st.write("Error! Enter name of car")
    else:
        st.write(f"""### The Price of {names} is {resp[0]}.""")
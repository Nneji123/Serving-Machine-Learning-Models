import streamlit as st
import json
import requests as re

st.title("Car Price Prediction Web App")

# st.image("image.png")

st.write("""
## About

**This Streamlit App utilizes a Machine Learning model served as an API to predict the price of a car based on certain features.** 

""")


st.header('# Input Car Details')

names = st.text_input("""Name of Car""")
curbweight= st.number_input("""Input Curb Weight""")
enginesize = st.number_input("""Input Engine Size""")
horsepower = st.number_input("""Input Horse Power""")
highwaympg= st.number_input("""Input Highway Miles Per Gallon""")
carwidth = st.number_input("""Input Car Width""")
wheelbase = st.number_input("""Input Wheel Base""")
drivewheel = st.number_input("""Input Drive Wheel""")
citympg = st.number_input("""Input City Miles Per Gallon""")
boreratio = st.number_input("""Input Bore Ratio""")
cylindernumber = st.number_input("""Input Cylinder Number""")

    



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
        st.write(f"""### The Price of the {names} is {resp[0]}$.""")
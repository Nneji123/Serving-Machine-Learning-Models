from flask import Flask, render_template, request
import utils

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        names = request.form["names"]
        symboling = int(request.form["symboling"])
        fueltype = int(request.form["fueltype"])
        aspiration = float(request.form["aspiration"])
        doornumber = float(request.form["doornumber"])
        carbody = float(request.form["carbody"])
        drivewheel = float(request.form["drivewheel"])
        enginelocation = float(request.form["enginelocation"])
        wheelbase = float(request.form["wheelbase"])
        carlength = int(request.form["carlength"])
        carwidth = int(request.form["carwidth"])
        carheight = float(request.form["carheight"])
        curbweight = float(request.form["curbweight"])
        enginetype = float(request.form["enginetype"])
        cylindernumber = float(request.form["cylindernumber"])
        enginesize = float(request.form["enginesize"])
        fuelsystem = float(request.form["fuelsystem"])
        boreratio = int(request.form["boreratio"])
        stroke = int(request.form["stroke"])
        compressionratio = float(request.form["compressionratio"])
        horsepower = float(request.form["horsepower"])
        peakrpm = float(request.form["peakrpm"])
        citympg = float(request.form["citympg"])
        highwaympg = float(request.form["highwaympg"])

        predicts = utils.predict_price(
            symboling,
            fueltype,
            aspiration,
            doornumber,
            carbody,
            drivewheel,
            enginelocation,
            wheelbase,
            carlength,
            carwidth,
            carheight,
            curbweight,
            enginetype,
            cylindernumber,
            enginesize,
            fuelsystem,
            boreratio,
            stroke,
            compressionratio,
            horsepower,
            peakrpm,
            citympg,
            highwaympg,
        )
        value = str(predicts)[1:-1]
    return render_template(
        "result.html", result=f"The Price of the {names} is: {value}$"
    )


if __name__ == "__main__":
    app.run(debug=True)

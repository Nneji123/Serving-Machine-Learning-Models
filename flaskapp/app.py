from flask import Flask, render_template, request
import utils

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        age = float(request.form["age"])
        anaemia = float(request.form["anaemia"])
        creatinine_phos = float(request.form["creatinine_phos"])
        diabetes = float(request.form["diabetes"])
        ejection = float(request.form["ejection"])
        hbp = float(request.form["hbp"])
        plat = float(request.form["plat"])
        serum_creatinine = float(request.form["serum_creatinine"])
        serum_sodium = float(request.form["serum_sodium"])
        sex = float(request.form["sex"])
        smoking = float(request.form["smoking"])
        time = float(request.form["time"])
        predicts = utils.predict_price(
            age,
            anaemia,
            creatinine_phos,
            diabetes,
            ejection,
            hbp,
            plat,
            serum_creatinine,
            serum_sodium,
            sex,
            smoking,
            time,
        )
        value = str(predicts)[1:-1]
        if value == 1:
            res = "Positive"
        else:
            res = "Negative"
    return render_template(
        "result.html", prediction_text="Predicted Outcome: {}".format(value)
    )


if __name__ == "__main__":
    app.run(debug=True)

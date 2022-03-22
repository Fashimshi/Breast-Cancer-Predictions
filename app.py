from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        features = [int(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)

        output = prediction
        final=[]
        for val in output:
        if val=2:
            final.append("Benign")
        else:
            final.append("Cancerous")

        return render_template('index.html', prediction_text='Your Cells are{}'.format(final))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

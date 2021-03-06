from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd


app = Flask(__name__)

loaded_model= pickle.load(open("model.pkl","rb"))

@app.route('/') 
@cross_origin()

def home():
    return render_template('index.html')

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    
    if request.method == "POST":
        features = [int(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = loaded_model.predict(final_features)

        output = round(prediction[0],1)
         
        

        return render_template('index.html', prediction_text='Your Cells are{}'.format(output))
    
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

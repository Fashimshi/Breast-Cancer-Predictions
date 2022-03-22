import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = prediction
    final=[]
    for val in output:
        if val=2:
            final.append("Benign")
        else: val=4:
            final.append("Cancerous")

    return render_template('index.html', prediction_text='Your Cells are{}'.format(final))

if __name__ == "__main__":
    app.run(debug=True)

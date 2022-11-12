import pickle
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
file_name = "static/finalized_model.sav"
ml_service = pickle.load(open(file_name,'rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/model", methods=['post'])
def model():
    height = np.int64(request.form['height'])
    result1 = ml_service.predict([[height]])[0]
    return f"<h1>Your predicted Weight <label style='color:red'>{result1}</label></h1>"

    

if __name__ == '__main__':
    app.run(debug=True)
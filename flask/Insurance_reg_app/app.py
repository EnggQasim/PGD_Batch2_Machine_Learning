from flask import Flask, request
import pandas as pd
import numpy as np
from pycaret.regression import * # step3

loaded_model = load_model("/home/mqasim/Data/NED/PGD Batch2 Machine Learning/flask/Insurance_reg_app/my_best_pipline")


app = Flask(__name__)

@app.route("/")
def index():
    return """
    <form action="/model" method="post">
    <h1>Insurance AI prediction Model</h1>
    <label>Age:</label> <input type="text" name="age"><br>
     <label>Sex:</label> <input type="text" name="sex"><br>
     <label>BMI:</label> <input type="text" name="bmi"><br>
     <label>Children:</label> <input type="text" name="chil"><br>
     <label>Smoker:</label> <input type="text" name="smk"><br>
     <label>Region:</label> <input type="text" name="region"><br>

     <input type="submit" value="Predict now">
    </form>
    """

@app.route("/model", methods=['POST'])
def about():
    age = np.int64(request.form['age'])
    sex = request.form['sex']
    bmi = np.float(request.form['bmi'])
    chil = np.int64(request.form['chil'])
    smk = request.form['smk']
    region = request.form['region']

    df = pd.DataFrame([[age,sex,bmi,chil,smk,region, 10]], columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'])
    print(df)
    df1 = predict_model(loaded_model,df)
    result = df1['Label'].values[0]

    return f"""
    Client age {age}<br>
    Client Sex {sex}<br>
    Client BMI {bmi}<br>
    Client children {chil}<br>
    Client Smooker {smk}<br>
    Client Region {region}<br>
    <h1>Predict Charges {result}</h1>
    """        

app.run(debug=True)

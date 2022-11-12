# Create Flask app and deploye on HeroKu server

## Step1:
* Create new Virtual Environment 
    * `pip install virtualenv`
        * activate on windows `.\abc\Scripts\activate`
        * activate on linux `source abc/bin/activate`
    * check packages names
        * `pip freeze > requirements.txt`
    * Install required packages
```
pip install flask numpy pandas gunicorn scikit-learn pickle5
```

# Step2:
* run **ML_class3.ipynb** -> save model file **finalized_model.sav**

# step3: Create your Flask App
1. create **app.py** file
2. create folder **static**
3. create folder **templates**

* open **app.py**
```
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
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
```

# final code for app.py
```
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
```
* **templates/index.html**
```
<h1>Height Vs Weight prediction Machine Learning Application</h1>
    <form method="post" action="/model">
        <h3>Enter your height in cm</h3><input type="text" name="height"><br>
        <input type="submit" value="Predict Weight"> 
    </form>
```

## Now time to deploy on HeroKu
* create your account on heroku
* create **Procfile**
    * `web: gunicorn app:app`
* create app on heroku and follow instructions
    * Download and install **herokucli**
    * `heroku login`
    * `git init`
    * `heroku git:remote -a <herokuAppname>`
    * 

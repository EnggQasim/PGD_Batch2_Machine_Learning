from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World! \
        Pakistan zinda bad\
        we love our country\
        "

@app.route("/about")
def about():
    return "<h1>About</h1> \
        Pakistan zinda bad\
        we love our country\
        "        

app.run(debug=True)

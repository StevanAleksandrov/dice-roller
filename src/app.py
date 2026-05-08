from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<string:name>")
def hello_world(name: str = None):
    return render_template("hello.html", _name=name)

# @app.route("/<name>")
# def personalized_hello(name):
#     return render_template("hello.html", _name=name)

@app.route("/dices")
def handle_dices():
    return "look at these beautiful dices"

# @app.route("/motivation")
# def motivation_txt():
#     return "Push through now, and you'll thank yourself later."
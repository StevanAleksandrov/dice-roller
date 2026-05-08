from flask import Flask, render_template , jsonify ,request

app = Flask(__name__)

@app.route("/")
@app.route("/<string:name>")
def hello_world(name: str = None):
    return render_template("hello.html", _name=name)


@app.route("/dices")
def handle_dices():
    return "look at these beautiful dices"

dices= [
    {"numberOfsides": 6},
    {"numberOFsides": 20}
]

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

dices = [
    {"numberOfSides": 6},
    {"numberOfSides": 20}
]


@app.route("/")
@app.route("/<string:name>")
def hello_world(name: str = None):
    return render_template("hello.html", _name=name, _author="Stevan Aleksandrov")


@app.route("/dices")
def handle_dices():
    return render_template("dices.html", _dices=dices, _author="Stevan Aleksandrov")


@app.route("/api/dices", methods=["GET", "POST"])
def handle_dice_request():

    if request.method == "GET":
        return jsonify(available_dices=dices)

    else:
        try:
            payload = request.json

            if not payload:
                raise Exception()

            if "numberOfSides" not in payload:
                raise Exception()

            if payload["numberOfSides"] <= 1:
                raise Exception()

            new_dice = {
                "numberOfSides": payload["numberOfSides"]
            }

            if new_dice in dices:
                raise Exception()

            dices.append(new_dice)

            return {"message": "dice created"}, 201

        except:
            return {"message": "An unknown error occurred"}, 500
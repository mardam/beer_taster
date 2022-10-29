from flask import Flask, render_template, request, redirect, url_for
from database.database import DatabaseConnector


app = Flask(__name__)
dc = DatabaseConnector("database/database.db")
port = 5000
ip = "192.168.178.28"
base_url = "http://" + ip + ":" + str(port)

@app.route("/<string:name>", defaults = {"beer_number": 1})
@app.route("/<string:name>/<int:beer_number>")
def form(name, beer_number):
    return render_template("form.html", name = name, beer_number = beer_number)

@app.route("/send_data", methods = ["POST"])
def send_data():
    if request.form["name"] == "Markus":
        dc.insert_beer(
                id = request.form["beer_number"],
                name = request.form["beer_name"],
                brand = request.form["beer_brand"],
                type = request.form["beer_type"])

    dc.insert_judgement(
            beer = request.form["beer_number"],
            user = request.form["name"],
            colour = request.form["colour"],
            foam = request.form["foam"],
            taste = request.form["taste"],
            posttaste = request.form["posttaste"],
            bottle = request.form["bottle"])
    return redirect(url_for("form", name = request.form["name"], beer_number = int(request.form["beer_number"]) + 1))

if __name__ == '__main__':
    app.run(port = port, debug = True, host = "0.0.0.0")

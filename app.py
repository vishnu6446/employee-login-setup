from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    emp_id = request.form["emp_id"]
    password = request.form["password"]

    if emp_id == "101" and password == "abc123":
        return render_template("success.html", emp_id=emp_id)
    else:
        return "Invalid Login"

app.run(debug=True)
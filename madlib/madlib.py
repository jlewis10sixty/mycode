#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/madlib")
def index():
    return render_template("madlib_form.html.j2")

@app.route("/finished")
def finished():
    return render_template("madlib.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

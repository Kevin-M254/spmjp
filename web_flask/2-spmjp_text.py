#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello spmjp!"


@app.route("/app", strict_slashes=False)
def spmjp():
    return "SPMJP"


@app.route('/spmjp/', defaults={'text': 'is_cool'})
@app.route('/spmjp/<text>', strict_slashes=False)
def display(text):
    """ Display spmjp, followed by some text """
    return "SPMJP {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

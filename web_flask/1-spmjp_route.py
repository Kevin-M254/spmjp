#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello spmjp!"


@app.route("/spmjp", strict_slashes=False)
def spmjp():
    return "SPMJP"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

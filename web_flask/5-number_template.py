#!/usr/bin/python3
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def num_display(n):
    """ Display n is a number """
    return "{} is a number".format(n)



@app.route('/number_template/<int:n>', strict_slashes=False)
def num_html(n):
    """ Display HTML template """
    return render_template('5-number.html', name=n)


@app.route('/number_odd_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ Display html page only if n is an integer """
    return render_template('6-number_odd_or_even.html', value=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

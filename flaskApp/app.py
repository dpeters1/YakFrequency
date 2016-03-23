from flask import Flask, render_template
import sys
import os.path
sys.path.append(os.path.join(os.path.split(os.path.dirname(os.path.abspath
                                                           (__file__)))[0],
                             "YikYak_Frequency"))
from sort import sortYaks

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html", yaks="No period selected")


@app.route("/<int:day>/<int:time>")
def time(day, time):
    sortedTuple = sortYaks(3, day, time)
    return render_template("index.html", yaks=sortedTuple)


if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0", debug=True)

from flask import Flask, render_template
import sys
import os.path
sys.path.append(os.path.relpath("../YikYak_Frequency",
                                os.path.dirname(os.path.abspath(__file__))))
from sort import sortYaks

app = Flask(__name__)


@app.route("/")
def main():
    sort = sortYaks(3, 17, 1)
    numbers = sort[1]
    numbers = [x for x in numbers if x > 1]
    # YakFreq = zip(sort[0], numbers)
    YakFreq = sort[0][0:len(numbers)]
    return render_template("index.html", yaks=YakFreq)

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template
import sys
sys.path.append("C:\Users\Dominic\Documents\YakFreq\YikYak_Frequency")
from sort_yaks import *
app = Flask(__name__)


@app.route("/")
def main():
    sort = sortYaks(3, 17, 1)
    numbers = sort[1]
    numbers = [x for x in numbers if x > 1]
    #YakFreq = zip(sort[0], numbers)
    YakFreq = sort[0][0:len(numbers)]
    return render_template("index.html", yaks=YakFreq)

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, request, jsonify
from datetime import datetime
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
    sortedTuple = sortYaks(1459656000, 1462075200, 4, 5, 17, 18, False, False)
    return render_template("index.html", yaks=sortedTuple)


@app.route('/timeData', methods=['POST', 'GET'])
def timeData():
    if request.method == 'POST':
        hourMin = request.json['hourMin']
        hourMax = request.json['hourMax']
        dayMin = request.json['dayMin']
        dayMax = request.json['dayMax']
        startDate = request.json['startStamp'] / 1000.0
        endDate = request.json['endStamp'] / 1000.0
        invertHour = request.json['invertHour']
        invertDay = request.json['invertDay']

        sortedShit = sortYaks(startDate, endDate, dayMin, dayMax, hourMin, hourMax, invertHour, invertDay)
        return jsonify(hourMin=hourMin, hourMax=hourMax, dayMin=dayMin, dayMax=dayMax, startDate=startDate, endDate=endDate, invertHour=invertHour, invertDay=invertDay, yaksup=sortedShit)


if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0", debug=True)

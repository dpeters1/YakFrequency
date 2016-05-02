import datetime
import os.path
from sort import sortYaks
'''
base_dir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
savePath = os.path.join(base_dir, "Word_Freq_Data")

def sortYaks(startDate, endDate, minDay, maxDay, minHour, maxHour, invertHour, invertDay):

    numDays = (endDate - startDate) / 86400
    dataset = []
    date = datetime.date.today()
    inRange = False

    for day in range(numDays):
        if not invertDay and day % 7 in range(minDay, maxDay + 1):
            date = datetime.datetime.fromtimestamp(startDate + 86400 * day)
            print date
            inRange = True

        elif invertDay and day % 7 not in range(minDay, maxDay + 1):
            date = datetime.datetime.fromtimestamp(startDate + 86400 * day)
            print date
            inRange = True

        if inRange:
            try:
                file = open(os.path.join(savePath, "wordData_" + str(date.month) +
                            "-" + str(date.day) + ".txt"), "r")
                print "Fetching words from wordData_" + str(date.month) + "-" + str(date.day) + ".txt"

                try:
                    for hour in range(0, 24):
                        file.seek(0, 0)
                        if not invertHour and hour in range(minHour, maxHour):
                            temp = file.readlines()[hour].split()
                            if temp != ['Empty']:
                                dataset += temp
                                print "Fetched yaks from %d:00" % hour
                        if invertHour and hour not in range(minHour, maxHour):
                            dataset += file.readlines()[hour].split()
                            print "Fetched yaks from %d:00" % hour

                except IndexError:
                    print "Index error; yaks were not collected at this time"
                file.close()
                print dataset
                inRange = False

            except IOError:
                print "Error: File not found"
'''

print sortYaks(1459656000, 1462075200, 4, 5, 17, 18, False, False)

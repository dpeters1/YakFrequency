from yaklient import *
import datetime
import os.path

carleton = Location(45.3856, -75.6959)
# Create user object at Carleton U with given userid
user = User(carleton, "6B6A473324AC4300B694BDA6C6287BE1")
today = datetime.date.today()
time = datetime.datetime.now()
base_dir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
savePath = os.path.join(base_dir, "Word_Freq_Data")
# Path of today's yak txt file
todayFile = os.path.join(savePath, "wordData_" + str(today.month) +
                         "-" + str(today.day) + ".txt")
# Needed if today's file is empty
yestFile = os.path.join(savePath, "wordData_" + str(today.month) +
                        "-" + str(today.day - 1) + ".txt")


def getLastYaks(fileName, hourTime):
    ''' Returns most recently stored yaks '''
    lastDataSet = []
    indexCount = 0
    file = open(fileName, "a+")

    for i in xrange(hourTime):
        file.seek(0, 0)
        try:
            lastDataSet = file.readlines()[hourTime - 1 - i].split("%^$ ")
        except IndexError:
            # Fill hours when program wasn't running with "Empty"
            indexCount += 1
            print "Index error, continuing operations"

        if lastDataSet != ['Empty\n'] and lastDataSet != []:
            # If yaks were found in the file, stop looking
            print "Going back %d hour(s) for last yaks" % (i + 1)
            break
    if hourTime - indexCount == 0:
        print "New or empty file"
    for j in xrange(indexCount):  # Fill previous hours' lines
            file.write("Empty\n")
    file.close()
    return lastDataSet


def getNewYaks(lastDataSet):
    ''' Pulls yaks from yikyak server and returns new ones '''
    wordData = []
    contentLen = len(user.get_yaks())

    for i, yak in enumerate(user.get_yaks()):
        post = str(yak)
        post = post[0:post.index('(')].lower()  # Remove karma rating

        if i + 1 == contentLen:
            break  # Skip the last yak about updating the app
        if post in lastDataSet:
            if wordData == []:
                print "No new yaks"
            else:
                print "New yaks: %s" % wordData
            break
        wordData.append(post)
    return wordData

# Iterate through previous hours' yaks until latest non-empty hour is found
lastDataSet = getLastYaks(todayFile, time.hour)

# Look in yesterday's yaks if none found in current day
if lastDataSet == []:
    lastDataSet = getLastYaks(yestFile, 24)
    print "Using yesterday's file"
# first line is from last hour

wordData = getNewYaks(lastDataSet)

file = open(todayFile, "a+")
if wordData == []:
    file.write("Empty\n")

else:
    print "Adding new yaks to file"
    file.write("%^$ ".join(wordData) + "%^$ " + "\n")

file.close()

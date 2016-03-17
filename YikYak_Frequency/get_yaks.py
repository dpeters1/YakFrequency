from yaklient import *
import datetime
import os.path

carleton = Location(45.3856, -75.6959)

# Create user object at Carleton U with given userid
user = User(carleton, "6B6A473324AC4300B694BDA6C6287BE1")
today = datetime.date.today()
time = datetime.datetime.now()
savePath = "C:\Users\Dominic\Documents\YakFreq\Word_Freq_Data"
fileName = os.path.join(savePath, "wordData_" + str(today.month) +
                        "-" + str(today.day) + ".txt")
yestFile = os.path.join(savePath, "wordData_" + str(today.month) +
                        "-" + str(today.day-1) + ".txt")
contentLen = len(user.get_yaks())
wordData = []

file = open(fileName, "a+")  # Create file if not present

if file.readline() == "" and time.hour == 0:  # Continued from yesterday
    yesterdayFile = open(yestFile, "r")
    for i in xrange(0, 24):
        yesterdayFile.seek(0, 0)
        lastDataSet = yesterdayFile.readlines()[23-i].split("%^$ ")
        if lastDataSet != ['Empty\n']:
            print "Going back %d hour(s) for last yaks" % (i+1)
            break
    print("New file, continuing from yesterday")
    yesterdayFile.close()

elif file.readline() == "":  # Empty file
    lastDataSet = []
    print("New file, non-continuing")
    file.seek(0, 0)  # Bring cursor back to start of file
    for i in xrange(0, time.hour):
        file.write("Empty\n")  # No yaks for all previous hours
else:
    # Iterate through previous hours' yaks until latest non-empty hour is found
    for i in xrange(0, time.hour):
        file.seek(0, 0)
        lastDataSet = file.readlines()[time.hour-1-i].split("%^$ ")
        if lastDataSet != ['Empty\n']:
            print "Going back %d hour(s) for last yaks" % (i+1)
            break
    print("Using existing file")
# first line is from last hour

for i, yak in enumerate(user.get_yaks()):
    post = str(yak)
    post = post[0:post.index('(')].lower()  # Remove karma rating

    if i+1 == contentLen:
        break  # Skip the yak about updating the app
    if post in lastDataSet:
        if wordData == []:
            print "No new yaks"
        else:
            print "New yaks: %s" % "|".join(wordData)
        break
    wordData.append(post)

if wordData != []:
    print "Adding new yaks to file"
    file.write("%^$ ".join(wordData) + "\n")

file.close()

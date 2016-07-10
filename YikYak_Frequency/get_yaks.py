import yaklient
import datetime
import os.path
import sys
from random import choice

university = "Carleton" # sys.argv[1]
coords = {
    "Carleton": [45.3856, -75.6959],
    "Toronto": [43.6629, -79.3957],
    "Queens": [40.7282, -73.7949],
    "Mcgill": [45.5048, -73.5772],
    "Ottawa": [45.4231, -75.6831],
    "Acadia": [45.0886, -64.3668],
    "Waterloo": [43.4723, -80.5449],
    "Algonquin": [45.3492, -75.7583],
    "Western": [43.0096, -81.2737],
}
userids = [
    "D96D24CC8FED432FBB1383D094806630",
    "8DA3792C333D4DD4A73D6BBB639B0F8C",
    "05EF6DB00E4A4DD4A57746841196C296",
    "AA002C6147EE491EBDD40ABC25368A53",
    "C4B30B02B949451BAC415F688386E2D0",
    "E3AECCCD723A4ECF91E6BA2234468CE1",
    "AE8BC5EEC3D24163AF7A61B688205666",
    "98F34C46A94B4A1AABB596FC258A9F68",
    "7B7F4A47A3604D25B9C7975494EAF0B0",
    "93B3778D5E9244B88A852CA266E988F4",
    "FBBC248C3BFF4653B46E7647B46280CC",
    "98DB944A80054AD18671BA003729D57B",
    "21FFD9CA4B0B4B2A9902B1334202E63A",
    "84B24906D0514FBE9B6E4CB76C393A4B",
    "7F440475CF634AFDA3AF8C4502F44BF8",
    "02DD40C5E8A746E0BFF9244BB44A8AF8",
    "E024AD2A7C0D4FE1AAA34179812454E2",
]
location = yaklient.Location(coords[university][0], coords[university][1])
# Create user object at Carleton U with given userid
user = yaklient.User(location, choice(userids))
today = datetime.date.today()
time = datetime.datetime.now()
base_dir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
savePath = os.path.join(base_dir, "Word_Freq_Data/" + university)
# Path of today's yak txt file
todayFile = os.path.join(savePath, "wordData_" + str(today.month) +
                         "-" + str(today.day) + ".txt")
# Needed if today's file is empty
yestFile = os.path.join(savePath, "wordData_" + str(today.month) +
                        "-" + str(today.day - 1) + ".txt")


def getLastYaks(fileName, hourTime):
    ''' Returns most recently stored yaks '''
    dataSet = []
    indexCount = 0
    file = open(fileName, "a+")

# Search file for last hour with content
    for i in xrange(hourTime):
        file.seek(0, 0)
        try:
            dataSet = file.readlines()[hourTime - 1 - i].split("%^$ ")
        except IndexError:
            # Fill hours when program wasn't running with "Empty"
            indexCount += 1
            print "Index error, continuing operations"

        if dataSet != ['Empty\n'] and dataSet != []:
            # If yaks were found in the file, stop looking
            print "Going back %d hour(s) for last yaks" % (i + 1)
            break
    if hourTime - indexCount == 0:
        print "New or empty file"
    for j in xrange(indexCount):  # Fill previous hours' lines
            file.write("Empty\n")
    file.close()
    return dataSet


def getNewYaks(lastDataSet, tries):
    ''' Pulls yaks from yikyak server and returns new ones '''
    dataSet = []
    endFound = False
    contentLen = len(user.get_yaks())

    for i, yak in enumerate(user.get_yaks()):
        post = str(yak)
        post = post[0:post.index('(')].lower()  # Remove karma rating

        if i + 1 == contentLen:
            break  # Skip the last yak about updating the app

        # Stop adding posts once the newest one from the previous data set
        # is found
        if post in lastDataSet:
            endFound = True
            if dataSet == []:  # Newest post is from the previous hour
                print "No new yaks"
            else:
                print "New yaks: %s" % dataSet
            break
        dataSet.append(post)

    # Only return posts if hour break point was found
    if endFound or tries > 2:
        return dataSet
    else:
        return 1

for i in xrange(4):
    ''' Create list of previous hours' posts, and only collect new posts.
    If all matching posts from previous hour are deleted, compare to
    the hour before that one '''

    # Iterate through previous hours' yaks until latest non-empty hour is found
    lastDataSet = getLastYaks(todayFile, time.hour - i)
    print "Iterating %i times" % (i + 1)
    # Look in yesterday's yaks if none found in current day
    if lastDataSet == [] or lastDataSet == ['Empty\n']:
        lastDataSet = getLastYaks(yestFile, 24 - i)
        print "Using yesterday's file"
        # first line is from last hour
    wordData = getNewYaks(lastDataSet, i)
    if wordData != 1:
        break

file = open(todayFile, "a+")
if wordData == []:
    file.write("Empty\n")

else:
    print "Adding new yaks to file"
    file.write("%^$ ".join(wordData) + "%^$ " + "\n")

file.close()

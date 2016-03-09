
# Should be run at the end of every hour (xx:59)
# to retreive the yaks from that hour.

from yaklient import *
from sort import *
import re
import datetime
import os.path

carleton = Location(45.3856, -75.6959)

# Create user object at Carleton U with given userid
user = User(carleton, "21C6CA60E3AA43C4B8C18B943394E111")
today = datetime.date.today()
time = datetime.datetime.now()
savePath = "C:\Users\Dominic\Documents\YakFreq\Word_Freq_Data"
fileName = os.path.join(savePath, "wordData_" + str(today.month) +
                        "-" + str(today.day) + ".txt")
yestFile = os.path.join(savePath, "wordData_" + str(today.month) +
                        "-" + str(today.day-1) + ".txt")
collection = ''
firstYak = ''
contentLen = len(user.get_yaks())
newContent = False

file = open(fileName, "a+")  # Create file if not present

if file.readline() == "" and time.hour == 0:  # Continued from yesterday
    yesterdayFile = open(yestFile, "r")
    firstLine = file.readlines()[46][0:10]
    print("New file, continuing from yesterday")
    yestFile.close()
elif file.readline() == "":  # Empty file
    firstLine = ""
    newContent = True
    print("New file, non-continuing")
    file.seek(0, 0)  # Bring cursor back to start of file
    for i in range(0, time.hour * 2):
        file.write("Empty \n")
else:
    file.seek(0, 0)
    firstLine = file.readlines()[time.hour*2-2][0:10]
    print("Using existing file")
# first line is from last hour


# Get yaks, iterate through them, and print them
for i, yaks in enumerate(user.get_yaks()):
    post = str(yaks)
    post = post[0:post.index('(')]  # Remove karma rating
    # print((post.lower()+"         ")[0:10] + "|" + firstLine + "|")

    # Appends the new set of words to the last set, without duplicates
    #                     _>Handles posts less than 10 chars
    if (post.lower()+"         ")[0:10] == firstLine:
        if i == 0:  # If first post is the same as last time
            newContent = False
            firstYak = firstLine
            print("No new content")
        else:
            newContent = True
            print("New content")
        break

    if i == 0:
        firstYak = post.lower()[0:10] + "         "
    if i+1 != contentLen:  # Skip the yak about updating the app
        collection += post.lower()  # Create one big string of posts

# Remove any words with apostraphes
fullWordList = collection.split()
for i, word in enumerate(fullWordList):
    for char in word:
        if ord(char) == 39:
            fullWordList.pop(i)
# Strip everything but alpha-numberic chars
wordList = removeStopwords(fullWordList, stopwords)
fullWordString = " ".join(wordList)
regexFullWordString = re.sub(r'([^\s\w]|_)+', '', fullWordString)

if newContent:
    print("New content added to file!")
    file.write(firstYak + "\n" + regexFullWordString + "\n")
if not newContent:  # Still add the first post identifier to that hour
    file.write(firstYak + "\n" + "Empty" + "\n")
file.close()

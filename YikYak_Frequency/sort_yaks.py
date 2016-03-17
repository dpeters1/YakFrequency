from sort import *
import os.path

savePath = "C:\Users\Dominic\Documents\YakFreq\Word_Freq_Data"


def sortYaks(month, day, time):
    file = open(os.path.join(savePath, "wordData_" + str(month) +
                "-" + str(day) + ".txt"), "r")

    try:
        dataSet = file.readlines()[time].split()
        if dataSet == ['Empty\n]']:
            print "No yaks posted at this hour"
        else:
            for i, word in enumerate(dataSet):
                for char in word:
                    if ord(char) == 39:
                        dataSet.pop(i)

            wordString = " ".join(removeStopwords(dataSet, stopwords))
            filtered = stripNonAlphaNum(wordString)
            dictionary = (wordListToFreqDict(filtered))
            sortedict = sortFreqDict(dictionary)
            sortedNum = (zip(*sortedict))[0]
            sortedWord = (zip(*sortedict))[1]
            return(sortedWord, sortedNum)

    except IndexError:
        print "Index error; yaks were not collected at this time"

sorted = sortYaks(3, 17, 1)  # Returns tuple containing sorted word list and
# corresponding word frequency list
if sorted != 0:
    for num in range(0, len(sorted[0])):
        if sorted[1][num] > 1:
            print("%s : %d" % (sorted[0][num], sorted[1][num]))

from sort import *
import os.path

savePath = os.path.relpath("../Word_Freq_Data")


def sortYaks(month, day, time):
    ''' Returns tuple containing sorted word list
        corresponding word frequency list '''
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
        return 0

sortedYaks = sortYaks(3, 17, 11)  # Returns tuple containing sorted word list
# corresponding word frequency list
if sortedYaks != 0:
    for num in range(0, len(sortedYaks[0])):
        if sortedYaks[1][num] > 1:
            print("%s : %d" % (sortedYaks[0][num], sortedYaks[1][num]))

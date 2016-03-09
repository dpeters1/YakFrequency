from sort import *
import os.path
savePath = "C:\Users\Dominic\Documents\YakFreq\Word_Freq_Data"


def sortYaks(month, day, time):
    file = open(os.path.join(savePath, "wordData_" + str(month) +
                "-" + str(day) + ".txt"), "r")
    content = file.readlines()[time*2+1]
    file.close()

    if content[0:5] == "Empty":
        print("No content at this hour")
        return 0
    wordlist = content.split()
    dictionary = (wordListToFreqDict(wordlist))
    sortedict = sortFreqDict(dictionary)
    sortedNum = (zip(*sortedict))[0]
    sortedWord = (zip(*sortedict))[1]

    return(sortedWord, sortedNum)


sorted = sortYaks(3, 9, 13)  # Returns tuple containing sorted word list and
# corresponding word frequency list
if sorted != 0:
    for num in range(0, len(sorted[0])):
        if sorted[1][num] > 1:
            print("%s : %d" % (sorted[0][num], sorted[1][num]))

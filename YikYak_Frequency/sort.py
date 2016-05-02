import os.path
import datetime

base_dir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
savePath = os.path.join(base_dir, "Word_Freq_Data")

stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your']
stopwords += ['yours', 'yourself', 'yourselves', 'like', 'just']


def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

# Given a list of words, return a dictionary of
# word-frequency pairs.


def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist, wordfreq))


# Sort a dictionary of word-frequency pairs in
# order of descending frequency.


def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


# Given a list of words, remove any that are
# in a list of stop words.

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]


def sortYaks(startDate, endDate, minDay, maxDay, minHour, maxHour, invertHour, invertDay):

    numDays = (endDate - startDate) / 86400  # Number of days in data range
    dataset = []
    date = datetime.date.today()
    inRange = False

    # Iterate through days
    for day in range(int(numDays)):
        if not invertDay and day % 7 in range(minDay, maxDay + 1):
            date = datetime.datetime.fromtimestamp(startDate + 86400 * day)
            # print date
            inRange = True

        elif invertDay and day % 7 not in range(minDay, maxDay + 1):
            date = datetime.datetime.fromtimestamp(startDate + 86400 * day)
            # print date
            inRange = True

        if inRange:
            try:
                file = open(os.path.join(savePath, "wordData_" + str(date.month) +
                            "-" + str(date.day) + ".txt"), "r")
                # print "Fetching words from wordData_" + str(date.month) + "-" + str(date.day) + ".txt"

                try:
                    for hour in range(0, 24):
                        file.seek(0, 0)
                        if not invertHour and hour in range(minHour, maxHour):
                            temp = file.readlines()[hour].split()
                            if temp != ['Empty']:
                                dataset += temp
                                # print "Fetched yaks from %d:00" % hour
                        elif invertHour and hour not in range(minHour, maxHour):
                            temp = file.readlines()[hour].split()
                            if temp != ['Empty']:
                                dataset += temp
                            # print "Fetched yaks from %d:00" % hour
                except IndexError:
                    pass
                    # print "Index error; yaks were not collected at this time"
                file.close()
                inRange = False
            except IOError:
                pass
                # print "Error: File not found"

    for i, word in enumerate(dataset):
        for char in word:
            if ord(char) == 39: # Remove words with apostraphes
                dataset.pop(i)

    wordString = " ".join(removeStopwords(dataset, stopwords))
    filtered = stripNonAlphaNum(wordString)
    dictionary = (wordListToFreqDict(filtered))
    sortedTuple = sortFreqDict(dictionary)

    return zip(*sortedTuple)

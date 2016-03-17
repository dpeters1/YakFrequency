from sys import argv
from sort import sortYaks

sortedYaks = sortYaks(int(argv[1]), int(argv[2]), int(argv[3]))
# corresponding word frequency list
if sortedYaks != 0:
    for num in range(0, len(sortedYaks[0])):
        if sortedYaks[1][num] > 1:
            print("%s : %d" % (sortedYaks[0][num], sortedYaks[1][num]))

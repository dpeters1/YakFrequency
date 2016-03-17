from sort import sortYaks

sortedYaks = sortYaks(3, 17, 11)  # Returns tuple containing sorted word list
# corresponding word frequency list
if sortedYaks != 0:
    for num in range(0, len(sortedYaks[0])):
        if sortedYaks[1][num] > 1:
            print("%s : %d" % (sortedYaks[0][num], sortedYaks[1][num]))

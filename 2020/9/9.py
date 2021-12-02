import sys
import re

# http://adventofcode.com/2020/day/9

data = []
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    rawin = int(rawin)
    if rawin:
        data.append(rawin)
#        print(rawin)
    else:
        pass

def checknum(number, checklist):
    for i in range(len(checklist)):
        for j in range(i+1, len(checklist)):
            if checklist[i] + checklist[j] == number:
                return True
    return False


for i, number in enumerate(data[25:]):
    if not checknum(number, data[i:i+25]):
        badnum = number
        break

print(badnum)

for i in range(len(data)):
    numlist = []
    tmpsum = 0
    j = 0
    while tmpsum < badnum:
        numlist.append(data[i+j])
        tmpsum += data[i+j]
        j += 1
    if tmpsum == badnum:
        print(min(numlist) + max(numlist))
        break

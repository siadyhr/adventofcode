import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/12

data = []
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        data.append(rawin)
#        print(rawin)
    else:
        pass

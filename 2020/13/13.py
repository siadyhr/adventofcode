import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/12
leave = int(input())
rawbus = input().split(",")
busses = [int(bus) for bus in rawbus if bus != "x"]
good_indices = [i for i, bus in enumerate(rawbus) if bus != "x"]
bad_indices = [i for i, bus in enumerate(rawbus) if bus == "x"]
new_busses = list(zip(good_indices, busses))
print(new_busses)

#data = []
#for rawin in sys.stdin:
#    rawin = rawin[:-1] # newlinestrip
##    print('"' + rawin + '"')
#    if rawin:
#        data.append(rawin)
##        print(rawin)
#    else:
#        pass

offset = 0
part1 = False
part2 = True
while part1:
    for bus in busses:
        if (leave + offset) % bus == 0:
            print(bus*offset)
            quit()
    offset += 1

# CRT
an = [
        (-a % n, n) for a, n in 
        sorted(new_busses, key=lambda x: (x[1], x[0]))
]
# Contains (a_i, n_i) -- find N så N = a_i mod n_i
print(an)
candidate = an[0][0]
increaser = 1
its = 0
for (ai, ni), (aj, nj) in zip(an, an[1:]):
    increaser = increaser * ni
    mult = 0
    print(ni)
    while True:
        its += 1
        if (candidate + mult*increaser)%nj == aj:
            candidate = candidate + mult * increaser
            break
        mult += 1
print("---")
print(its)
print([candidate % ni for _,ni in an])
print(candidate)
quit()
candidate = 0
while part2:
    if candidate % 19**5 == 0:
        print(candidate//19**5)
#    print([
#        (candidate + bus[0]) % bus[1] == 0
#        for bus in new_busses
#        ])
    if all([
        (candidate + bus[0]) % bus[1] == 0
        for bus in new_busses
        ]):
        print(candidate)
        quit()
    candidate += busses[0]

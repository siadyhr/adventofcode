import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/11

seats = []
tolerance = 5
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        seats.append(rawin)
#        print(rawin)
    else:
        pass

directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
oldseats = copy.deepcopy(seats)
def get_nearby(data, row, col):
    nearby = {}
    for direction in directions:
        if row+direction[1] < 0 or row+direction[1] >= len(data):
            continue
        if col+direction[0] < 0 or col+direction[0] >= len(data[row]):
            continue
#        print(direction)
#        print(data[row+direction[1]])#[col+direction[0]])
        nearby[direction] = data[row+direction[1]][col+direction[0]]
#    print(nearby)
    return nearby

def fancy_get_nearby(data, row, col):
    nearby = {}
    for direction in directions:
        hit = "."
        n = 1
        while hit not in "#L":
            newdir = [n*x for x in direction]
            if row+newdir[1] < 0 or row+newdir[1] >= len(data):
                break
            if col+newdir[0] < 0 or col+newdir[0] >= len(data[row]):
                break
            hit = data[row+newdir[1]][col+newdir[0]]
            n += 1
#        print(direction)
#        print(data[row+direction[1]])#[col+direction[0]])
        nearby[direction] = hit #data[row+direction[1]][col+direction[0]]
#    print(nearby)
    return nearby


iterations = 0
updated = {x : True for x in directions}
while True:
    print(iterations)
    newseats = []
    for row in range(len(oldseats)):
        newseats.append("")
        for col in range(len(oldseats[0])):
#            if not any([
#                updated.get(
#                    (row+direction[0], col+direction[1]), False) for direction in directions]
#                ):
#                continue

#            nearby = get_nearby(oldseats, row, col)
            nearby = fancy_get_nearby(oldseats, row, col)
#            if len(nearby) < 8:
#                print("!\t", nearby)
#            print(row, col, oldseats[row][col], nearby)
            if oldseats[row][col] == "L" and all([seat != "#" for seat in nearby.values()]):
#                print("L->#")
                newseats[-1] += "#"
            elif oldseats[row][col] == "#" and sum([seat == "#" for seat in nearby.values()]) >= tolerance:
#                print("#->L")
                newseats[-1] += "L"
            else:
#                print("None")
                newseats[-1] += oldseats[row][col]
    for line in newseats:
        print(line)
    if newseats == oldseats:
        break
    else:
        oldseats = [line for line in newseats]

    iterations += 1

n_occupied = 0
for row in range(len(newseats)):
    for col in range(len(newseats[0])):
        if newseats[row][col] == "#":
            n_occupied += 1
print()
print(n_occupied)

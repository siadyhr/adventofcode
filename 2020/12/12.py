import sys
import re
import functools
import copy
import numpy as np
import numpy.linalg

# http://adventofcode.com/2020/day/12

data = []
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        data.append((rawin[0], int(rawin[1:])))
#        print(rawin)
    else:
        pass

facing = 0 # pi/2 radianer
position = np.array([0, 0], dtype=int)
wayp = np.array([10,1], dtype=int)
rotations = {
        "L" : 1,
        "R" : -1
        }
rotmat = np.array([
    [0, -1],
    [1, 0]
    ], dtype=int)
directions = [np.array(x) for x in [[1,0], [0,1], [-1,0], [0,-1]]]
movements = {
        label : np.array(x)
        for label, x in zip(
            ["E", "N", "W", "S"],
            directions
            )
        }
for instruction in data:
    print(instruction)
    if instruction[0] in "ENWS":
        wayp = wayp + movements[instruction[0]] * instruction[1]
    elif instruction[0] == "F":
#        position = position + (wayp - position) * instruction[1]
        position = position + wayp * instruction[1]
    elif instruction[0] in "LR":
#        facing = (facing + rotations[instruction[0]] * instruction[1]//90) % 4
        nrots = rotations[instruction[0]] * instruction[1]//90
#        wayp = position + numpy.linalg.matrix_power(rotmat, nrots%4) @ (wayp-position)
        wayp = numpy.linalg.matrix_power(rotmat, nrots%4) @ (wayp)
    else:
        print("!")
    print(position, wayp)
print(position, sum([abs(x) for x in position]))

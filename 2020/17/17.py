import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/17

data = []
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        data.append(rawin)
#        print(rawin)
    else:
        pass
print(data)
n_turns = 6
def create_labyrinth(data, n_turns):
    labyrinth = []
    for z in range(2*n_turns + 1):
        z_list = []
        for x in range(2*n_turns + len(data)):
            x_list = []
            for y in range(2*n_turns + len(data)):
                if z == n_turns and x-n_turns >= 0 and y-n_turns >= 0:
                    try:
                        x_list.append(
                                1 if data[x-n_turns][y-n_turns] == "#" else 0
                        )
                    except IndexError:
                        x_list.append(0)
                else:
                    x_list.append(0)
            z_list.append(x_list)
        labyrinth.append(z_list)
    return labyrinth

def get_neighbours(data, x, y, z):
#    neighbours = {}
    N = 0
    ds = [-1, 0, 1]
    for dx in ds:
        for dy in ds:
            for dz in ds:
                if not (dx==0 and dy==0 and dz==0):
                    try:
                        if x+dx >= 0 and y+dy >= 0 and z+dz >= 0:
                            N += data[z+dz][y+dy][x+dx]
#                                neighbours[(dx,dy,dz)] = data[x][y][z]
                    except IndexError:
                        pass
    return N


def simulate_labyrinth(data, n_sims):
    old_labyrinth = data
    for _ in range(n_sims):
        new_labyrinth = []
        for z, layer in enumerate(old_labyrinth):
            new_layer = []
            for y, y_line in enumerate(layer):
                new_line = []
                for x, xval in enumerate(y_line):
                    N = get_neighbours(old_labyrinth, x, y, z)
                    if xval:
                        new_line.append(
                            1 if 2 <= N <= 3 else 0
                        )
                    else:
                        new_line.append(
                                1 if N == 3 else 0
                        )
                new_layer.append(new_line)
            new_labyrinth.append(new_layer)
        old_labyrint = None
        old_labyrinth = copy.deepcopy(new_labyrinth)
    return old_labyrinth

def print_labyrinth(labyrinth):
    for layer in labyrinth:
        for line in layer:
            print(" ".join(str(x) for x in line))
        print()

def sum_labyrinth(labyrinth):
    layersums = [
            [sum(line) for line in layer] for layer in labyrinth
        ]
    return sum([sum(layersum) for layersum in layersums])

labyrinth = create_labyrinth(data, n_turns)
#print_labyrinth(labyrinth)
#x = n_turns + 0
#y = n_turns + 0
#z = n_turns + 1
#print(labyrinth[z][y][x])
#print(get_neighbours(labyrinth, x, y, z))
new_lab = simulate_labyrinth(labyrinth, n_turns)
print(sum_labyrinth(new_lab))
#print_labyrinth(new_lab)
#for y, y_list in enumerate(data):
#    a = []
#    for x, xval in enumerate(y_list):
#        print(x, y, labyrinth[1][y+1][x+1], get_neighbours(labyrinth, x+1, y+1, 1))

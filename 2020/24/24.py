import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/24

instructions = []
tiles = {}
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        instruction = []
        it = iter(rawin)
        for char in it:
            if char in "ew":
                instruction.append(char)
            else:
                instruction.append(char + next(it))
#        print(instruction)
        instructions.append(instruction)
    else:
        pass

directions = ["e", "w", "ne", "nw", "se", "sw"]

def move_on_grid(instruction, start):
    position = start
    if type(position) is tuple:
        position = list(position)
    for order in instruction:
        if order == "e":
            position[0] += 1
        elif order == "w":
            position[0] -= 1
        elif order == "ne":
            if position[1] % 2 == 1:
                position[0] += 1
            position[1] -= 1
        elif order == "nw":
            if position[1] % 2 == 0:
                position[0] -= 1
            position[1] -= 1
        elif order == "se":
            if position[1] % 2 == 1:
                position[0] += 1
            position[1] += 1
        elif order == "sw":
            if position[1] % 2 == 0:
                position[0] -= 1
            position[1] += 1
    return position

def flip_grid(instructions, tiles):
    for instruction in instructions:
        destination = tuple(move_on_grid(instruction, [0, 0]))
        if destination in tiles:
            tiles[destination] = not tiles[destination]
        else:
            tiles[destination] = True
    return tiles

def count_blacks(tiles):
    return sum(tiles.values())

def get_neighbours(tile, tiles):
    directions = ["e", "w", "ne", "nw", "se", "sw"]
    return [tiles.get(tuple(move_on_grid([direction], tile)), 0) for direction in directions]

def evolve_grid(tiles):
    new_grid = {}
    directions = ["e", "w", "ne", "nw", "se", "sw"]
    new_tiles = []
    for tile in tiles:
        neighbours = [tuple(move_on_grid([direction], tile)) for direction in directions]
        for neighbour in neighbours:
            if not neighbour in tiles:
                new_tiles.append(neighbour)
    for new_tile in new_tiles:
        tiles[new_tile] = False
    for tile, color in tiles.items():
        n_neighbours = sum(get_neighbours(tile, tiles))
        if color:
            if (n_neighbours == 0 or n_neighbours > 2):
                new_grid[tile] = False
            else:
                new_grid[tile] = True
        else:
            if n_neighbours == 2:
                new_grid[tile] = True
            else:
                new_grid[tile] = False
    return new_grid

def evolve_grid_n(tiles, time):
    for _ in range(time):
        tiles = evolve_grid(tiles)
    return tiles

print("Part 1")
base_tiles = flip_grid(instructions, tiles)
print(count_blacks(base_tiles))

print("\nPart 2")
print(count_blacks(evolve_grid_n(base_tiles, 100)))

import sys
import re
import functools
import copy
import solution_magic
import numpy as np

# http://adventofcode.com/2020/day/20

raw_tiles = {}
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
    if "Tile" in rawin:
        tile_id = int(rawin[5:-1])
        tile = []
    elif rawin:
        tile.append([1 if x == "#" else 0 for x in rawin])
    else:
        raw_tiles[tile_id] = tile #np.array(tile)

tiles = {}
for tile_id, tile in raw_tiles.items():
    # Orienteret højre om
    tiles[tile_id] = (
        # top
        tile[0],
        # right
        [line[-1] for line in tile],
        # bottom
        tile[-1][::-1],
        # left
        [line[0] for line in tile[::-1]],
        # top, flippet om |
        tile[0][::-1],
        # right
        [line[0] for line in tile],
        # bottom
        tile[-1],
        # left
        [line[-1] for line in tile[::-1]],
    )

#free_edges = {}
#for tile_id, tile in tiles.items():
#    goods = ()
#    for i, edge in enumerate(tile):
#        other_edges:
#        if edge not in [edge for key, value in tiles.items() for edge in value if key != tile_id]:
#            goods += (i,)
#    if goods:
#        free_edges[tile_id] = goods
size = int(len(tiles)**0.5)

def get_side(orientation, side):
    # side: 0, 1, 2, 3
    if orientation < 4:
        return (orientation + side) % 4
    return 4 + ((orientation - 4 + side) % 4)

def add_piece(puzzle, i, j):
    # puzzle er dict {(i, j) : (tile_id, orientation)}
    # orientation er offset for at få top (intet ~ 0)
    for tile_id, piece in tiles.items():
        if tile_id in [x[0] for x in puzzle.values()]:
            continue
        for orientation in range(8):
            if (
                # Venstre/højre
                j == 0 or tiles[
                        puzzle[i,j-1][0]
                    ][
                        get_side(puzzle[i, j-1][1], 1)
                    ] == piece[get_side(orientation, 3)][::-1]
                ) and (
                # Top/bund
                i == 0 or tiles[
                        puzzle[i-1,j][0]
                    ][
                        get_side(puzzle[i-1, j][1], 2)
                    ] == piece[get_side(orientation, 0)][::-1]
                ):
                    puzzle[i, j] = (tile_id, orientation)
                    yield puzzle

def nextij(i, j):
    if j < size-1:
        return (i, j+1)
    return (i+1, 0)

def solve(puzzle, i=0, j=0, depth=0):
#    print(depth*"  " + "%s, [%s, %s]" % (puzzle, i, j))
    if i == size: # Vi er færdige
#        print("Done!", puzzle)
        global solution
        solution = puzzle
        return True
    # Sæt brikker i
    possibilities = []
    for p in add_piece(puzzle, i, j):
        possibilities.append(copy.deepcopy(p))
    return True if any(
            solve(subpuzz, *nextij(i, j), depth+1)
            for subpuzz in possibilities
            ) else False
#    for subpuzz in add_piece(puzzle, i, j):
##        print(subpuzz)
#        # Ellers, sæt brikker i resten
#        possibility = solve(subpuzz, *nextij(i, j), depth+1)
#        print(">>"*depth, possibility)
#        if possibility:
#            return possibility
#    # Vi er her hvis man ikke kunne sætte brikker i

part = 2
if part == 1:
    solve({})
    print(solution)
    corners = [solution[0,0], solution[0, size-1], solution[size-1, 0], solution[size-1, size-1]]
    result = 1
    for corner in corners:
        result *= corner[0]

    print(result)
    quit()

raw_atlas = solution_magic.get_solution()
#solve({})
#raw_atlas = solution
def get_oriented_tile(tile, orientation):
#    print(tile)
    if orientation == 0:
        return tile
    if orientation == 1:
        tile = np.array(tile)
        return [list(tile[:,i]) for i in range(len(tile[0]))[::-1]]
    elif 1 < orientation < 4:
        return get_oriented_tile(
                get_oriented_tile(tile, 1),
                orientation - 1
            )
    elif orientation == 4:
        return [line[::-1] for line in tile]
    else: # orientation > 4
        return get_oriented_tile(
                get_oriented_tile(tile, 4),
                orientation-4
        )

def print_tile(tile):
    if type(tile) is int:
        tile = raw_tiles[tile]
    for line in tile:
        print(" ".join([str(x) for x in line]))

def create_atlas():
    atlas = []
    for row in range(10*size):
        if row%10 in [0,9]:
            continue
        line = []
        for chart_col in range(size):
#            print(row, chart_col)
            current_tile = get_oriented_tile(
                    raw_tiles[raw_atlas[row//10,chart_col][0]],
                    raw_atlas[row//10,chart_col][1]
                    )
#            print_tile(current_tile)
            line += current_tile[row%10][1:-1]
        atlas.append(line)
    return atlas

atlas = get_oriented_tile(create_atlas(), 0)

seamonster = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1], 
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0] 
]
def compare_line(key, sample):
    return all(y for x, y in zip(key, sample) if x)

def find_seamonster(atlas, i, j):
    sample = [
            [atlas[i+di][j+dj] for dj in range(20)]
            for di in range(3)
    ]
#    print_tile(sample)
    return all(
            compare_line(key, sample)
            for key, sample in zip(seamonster, sample)
    )

#print_tile(atlas)
def find_seamonsters(atlas):
    seamonster_locations = {}
    for i in range(len(atlas) - 2):
        for j in range(len(atlas[0]) - 19):
            if find_seamonster(atlas, i, j):
                sample = [
                        [atlas[i+di][j+dj] for dj in range(20)]
                        for di in range(3)
                ]
                print_tile(sample)
                print()
                hashtags = sum(sum(line) for line in sample)
                seamonster_locations[(i, j)] = hashtags
    return seamonster_locations

def pretty_print_atlas(atlas, seamonsters):
    print("Pretty print ♥")
    for i, line in enumerate(atlas):
        atlas[i] = [" " if x else "\033[34m~" for x in line]
    pretty_seamonster = [
            r"   _   _   O>",
            r"\ / \ / \ /  "
    ]
    
    ugly_seamonster = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], # 3 × 20
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1], 
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0] 
    ]
    pretty_seamonster = [
            ["\033[35;1m" + x if x else " " for x in line]
            for line in pretty_seamonster
            ]
    semi_pretty_seamonster = [
            ["\033[35;1mO" if x else " " for x in line]
            for line in ugly_seamonster
    ]
    almost_pretty_seamonster = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "_", 0], # 3 × 20
        ["_", 0, 0, 0, 0, "_", "_", 0, 0, 0, 0, "_", "_", 0, 0, 0, 0, "/", "O", ">"], 
        [0, "\\", 0, 0, "/", 0, 0, "\\", 0, 0, "/", 0, 0, "\\", 0, 0, "/", 0, 0, 0] 
    ]
    almost_pretty_seamonster = [
            ["\033[35;1m" + x if x else " " for x in line] for line in almost_pretty_seamonster
    ]
    usethis_seamonster = almost_pretty_seamonster
    for seamonster in seamonsters[0]:
        print(seamonster)
        for drow in range(3):
            for dcol in range(20):
                if usethis_seamonster[drow][dcol] != " ":
                    atlas[seamonster[0] + drow][seamonster[1] + dcol] = usethis_seamonster[drow][dcol]
    for line in semi_pretty_seamonster:
        print("".join(line))
    for line in atlas:
        print("".join(line))

def find_all_seamonsters(atlas):
    all_seamonsters = []
    for orientation in range(8):
        all_seamonsters.append(find_seamonsters(
            get_oriented_tile(atlas, orientation)
        ))
    return all_seamonsters
all_seamonsters = find_all_seamonsters(atlas)
n_monsters = sum(len(x) for x in all_seamonsters)
n_hashtags = sum(sum(line) for line in atlas)
print(n_hashtags)
print(n_monsters)
print(n_hashtags - n_monsters*15)
print(all_seamonsters)
pretty_print_atlas(
    get_oriented_tile(atlas, *[i for i, x in enumerate(all_seamonsters) if x]),
    [x for x in all_seamonsters if x]
)

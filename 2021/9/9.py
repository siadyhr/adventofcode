import sys
import queue
from operator import mul
from functools import reduce

def get_neighbour_ids(x, y):
    if x > 0:
        yield (x - 1, y)
    if y > 0:
        yield (x, y - 1)
    if x < xmax - 1:
        yield (x + 1, y)
    if y < ymax - 1:
        yield (x, y + 1)

def is_low(heightmap, choords):
    return all(
        heightmap[choords[0]][choords[1]] < heightmap[x][y]
        for x, y in get_neighbour_ids(*choords)
    )

def low_points(heightmap):
    for x0 in range(xmax):
        for y0 in range(ymax):
            if (is_low(heightmap, (x0, y0))):
                yield heightmap[x0][y0]

def part1(heightmap):
    return sum(x + 1 for x in low_points(heightmap))

def get_basin(heightmap, choords):
    to_visit = queue.Queue()
    to_visit.put(choords)
    visited = [[False for _ in range(ymax)] for __ in range(xmax)]
    while not to_visit.empty():
        x,y = to_visit.get()
        if heightmap[x][y] == 9 or visited[x][y]:
            continue

        for c in get_neighbour_ids(x, y):
            to_visit.put(c)
        visited[x][y] = True
        yield (x, y)

def get_basins(heightmap):
    basins = [[-1 for _ in range(ymax)] for __ in range(xmax)]
    basins_lookup = {}
    basin_sizes = []
    basin_id = 0
    for x0 in range(xmax):
        for y0 in range(ymax):
            if heightmap[x0][y0] == 9 or basins[x0][y0] != -1:
                continue
            basin_size = 0
            for x,y in get_basin(heightmap, (x0, y0)):
                basin_size += 1
                basins[x][y] = basin_id
                try:
                    basins_lookup[basin_id].append((x, y))
                except KeyError:
                    basins_lookup[basin_id] = [(x, y)]
            basin_sizes.append(basin_size)
            basin_id += 1
    return basins_lookup, basin_sizes

def part2(heightmap):
    lookup, sizes = get_basins(heightmap)
    return reduce(
            mul,
            (x[1] for x in sorted(
                enumerate(sizes),
                key=lambda x: x[1],
                reverse=True)[:3]
            )
        )

heightmap = []
for line in sys.stdin:
    heightmap.append([int(x) for x in line[:-1]])

# x down, y to the right…
xmax = len(heightmap)
ymax = len(heightmap[0])

print(part1(heightmap))
print(part2(heightmap))

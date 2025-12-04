import sys
rawdata = [line[:-1] for line in sys.stdin]
rolls = {}

width = len(rawdata[0])
height = len(rawdata)

result = 0
result2 = 0

directions8 = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)
        ]

def oob(i, j):
    return (i<0 or i>=height) or (j<0 or j>=height)

for i, line in enumerate(rawdata):
    for j, x in enumerate(line):
        if x == "@":
            rolls[(i, j)] = [0, []]
            for direction in directions8:
                neighbour = (i + direction[0], j + direction[1])
                if oob(*neighbour):
                    continue
                if rawdata[neighbour[0]][neighbour[1]] == "@":
                    rolls[(i, j)][0] += 1
                    rolls[(i, j)][1].append(neighbour)

for roll, (n_neighbours, _) in rolls.items():
    if n_neighbours < 4:
        result += 1

while min(n_neighbours for (n_neighbours, _) in rolls.values()) < 4:
    to_update = []
    for roll, (n_neighbours, neighbours) in rolls.items():
        if n_neighbours < 4:
            to_update.append((roll, neighbours))
    if not to_update:
        print([x for (x,_) in rolls.values()])
    for roll, neighbours in to_update:
        rolls.pop(roll)
        result2 += 1
        for neighbour in neighbours:
            rolls[neighbour][0] -= 1
            idx = rolls[neighbour][1].index(roll)
            rolls[neighbour][1].pop(idx)


print(result)
print(result2)

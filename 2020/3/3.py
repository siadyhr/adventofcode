from operator import mul
from functools import reduce

forest = []
while True:
    rawin = input()
    if rawin:
        forest.append(rawin)
    else:
        break
#print(forest)

accidents = []
width = len(forest[0])
paths = [(1,1), (3,1), (5,1), (7,1), (1,2)]

for n_path, path in enumerate(paths):
    row = 0
    column = 0
    accident = 0
    while row < len(forest):
        if forest[row][column] == "#":
            accident += 1
        column = (column + path[0]) % width
        row += path[1]
    accidents.append(accident)

print(accidents)
print(reduce(mul, accidents, 1))

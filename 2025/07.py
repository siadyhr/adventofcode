import sys
import functools
result = 0
result2 = 0

# 06.21
rawdata = [line[:-1] for line in sys.stdin]
start = rawdata[0].index("S")
queue = [(0, start)]
visited = {}
print(queue)

while queue:
    (i, j) = queue.pop()
    if i + 1 == len(rawdata):
        continue
    if rawdata[i+1][j] == "^":
        if (i+1, j) in visited:
            continue
        else:
            visited[(i+1, j)] = True
            queue += [(i+1, j-1), (i+1, j+1)]
            result += 1
    else:
        queue.append((i+1, j))

@functools.cache
def n_paths(i, j):
    if i + 1 == len(rawdata):
        return 1
    if rawdata[i][j] == "^":
        return n_paths(i+1, j-1) + n_paths(i+1, j+1)
    return n_paths(i+1, j)

print(result) #07.21; t+6
print(n_paths(0, start)) #07.33; t+12

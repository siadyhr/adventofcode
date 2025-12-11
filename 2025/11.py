# 07.41
import sys
import functools
graph = {}
for line in sys.stdin:
    node, neighbours = line.split(":")
    neighbours = neighbours.strip().split()
    graph[node] = neighbours

def n_paths(graph, a, b):
    if a == b:
        return 1
    return sum(n_paths(graph, neighbour, b) for neighbour in graph[a])

result = n_paths(graph, "you", "out")
print("Part 1", result) #07.47

@functools.cache
def n_paths_visiting(a, b, dac_visited, fft_visited):
    if a == b:
        if dac_visited and fft_visited:
            return 1
        return 0
    if a == "dac":
        return sum(n_paths_visiting(neighbour, b, True, fft_visited) for neighbour in graph[a])
    elif a == "fft":
        return sum(n_paths_visiting(neighbour, b, dac_visited, True) for neighbour in graph[a])
    else:
        return sum(n_paths_visiting(neighbour, b, dac_visited, fft_visited) for neighbour in graph[a])

result2 = n_paths_visiting("svr", "out", False, False)
print("Part 2", result2) #07.54

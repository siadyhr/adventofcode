import sys
graph = {}
capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for line in sys.stdin:
    a, b = line[:-1].split('-')
    try:
        graph[a].append(b)
    except KeyError:
        graph[a] = [b]
    try:
        graph[b].append(a)
    except KeyError:
        graph[b] = [a]


print(graph)
journeys = []

"""
visited = {
        key : False
        for key in graph.keys() if all(x not in capitals for x in key)
        }
print(visited)
"""
to_visit = ['start']

# Rekursiv funktion: Returner alle stier
# En generator af [a, b, c, d]'er

def visit(start, visited):
    for neighbour in graph[start]:
        if neighbour == 'end':
            yield [start]
        elif neighbour[0] in capitals or neighbour not in visited:
            for path in visit(neighbour, visited + [start]):
                yield [start] + path

paths = set()
for path in visit('start', []):
    paths |= set((tuple(path), ))

def print_path(path):
    print("-".join(path) + "-end")

for path in paths:
    print_path(path)
print(len(paths))

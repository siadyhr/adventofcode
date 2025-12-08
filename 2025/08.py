import sys
result = 0
result2 = 0

#07.05
data = [tuple(map(int, line[:-1].split(","))) for line in sys.stdin]

distances = []

def dist(p, q):
    return sum((x-y)**2 for (x,y) in zip(p, q))

for i, p in enumerate(data):
    for j,q in enumerate(data[i+1:], i+1):
        distances.append( ((i, j), dist(p, q)) )

distances.sort(key = lambda (x, y) : (y, x))
(i, j), _ = distances[0]
print(data[i], data[j], _)
graph = {}
n_connections = 0
for (i, j), _ in distances:
#    if n_connections == 10:
#    if n_connections == 1000:
#    # Part 1 break condition
#        break
    if j in graph.get(i, []):
        n_connections += 1
        # Case: Already indirectly connected
        continue

    # Otherwise, connect them
    # That is, add i and all its neighbours
    # to j and all its neighbours and <->
    n_connections += 1
    tmp = graph.get(i, set()).copy() 
    for k in tmp:
        graph[k] |= set([j])
        graph[k] |= graph.get(j, set())
    tmp = graph.get(j, set()).copy() 
    for k in tmp:
        graph[k] |= set([i])
        graph[k] |= graph.get(i, set())

    graph[i] = graph.get(i, set()) | set([j])
    graph[j] = graph.get(j, set()) | set([i])

    graph[i] |= graph.get(j, set())
    graph[j] |= graph.get(i, set())

    # Have we connected everything now?
    if len(graph.get(0, [])) == len(data):
        # Part 2. Done 07.56
        print("Break")
        print(graph.get(0, []))
        print(len(data))
        result2 = data[i][0] * data[j][0]
        print(data[i])
        print(data[j])
        print("Part 2", result2)
        break

    
#print(graph)
subgraphs = set(frozenset(x) for x in graph.values())
subgraph_lengths = sorted((len(g) for g in subgraphs), reverse=True)
result = subgraph_lengths[0] * subgraph_lengths[1] * subgraph_lengths[2]
#print(subgraphs)
#print(subgraph_lengths)
print(result) #7.50
print(result2)

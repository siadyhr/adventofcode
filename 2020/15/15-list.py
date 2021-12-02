# http://adventofcode.com/2020/day/15

data = [int(x) for x in input().split(",")]
print(data)
#N = 2020
N = 30000000

#visited = {num : index for index, num in enumerate(data[:-1])}
visited = N * [None]
print("initialiseret")
#print(visited)
for index, num in enumerate(data[:-1]):
    visited[num] = index

lastnum = data[-1]
for index in range(len(data) - 1, N-1):
#    print("i: %s, num: %s" % (index, lastnum))
    if visited[lastnum] is not None:
        offset = index - visited[lastnum]
        visited[lastnum] = index
        lastnum = offset
#        print("\tVisited %s ago" % offset)
    else:
#        print("\tNot visited")
        visited[lastnum] = index
        lastnum = 0
#    print(visited)
#    print(lastnum)
print(lastnum)

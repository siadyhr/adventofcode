# http://adventofcode.com/2020/day/15

data = [int(x) for x in input().split(",")]
print(data)

visited = {num : index for index, num in enumerate(data[:-1])}
print(visited)
lastnum = data[-1]
for index in range(len(data) - 1, 30000000-1):
#    print("i: %s, num: %s" % (index, lastnum))
    if lastnum in visited:
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

import sys
import re
import functools

# http://adventofcode.com/2020/day/10

data = []
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    rawin = int(rawin)
    if rawin:
        data.append(rawin)
#        print(rawin)
    else:
        pass
data.sort()
#print(data[:10])
ones = 0
threes = 0
for prevnum, num in zip([0] + data, data + [max(data) + 3]):
    if num - prevnum == 1:
        ones += 1
    elif num - prevnum == 3:
        threes += 1
#print(ones*threes)

def connect(rating, adapters, depth=0):
    if len(adapters) == 1:
#        print("End!")
#        print(depth*" ", adapters)
        return 1
    else:
        tmplist = []
#        print(len(adapters), adapters[:10])
        for i, adapter in enumerate(adapters):
            if adapter - rating <= 3:
#                print(depth*" " + str(adapter))
                x = connect(adapter, adapters[i+1:], depth+1)
                tmplist.append(x)
            else:
#                print("Break: %s/%s" % (adapter, rating))
                break
        return sum(tmplist)

def n_goods(adapters):
    out = 0
    for adapter in adapters[1:]:
        if (adapters[0] - adapter) <= 3:
            out += 1
        else:
            break
    return out

#perms = 1
#for i, adapter in enumerate(data[::-1]):
#    print(adapter)
#    print("\t", data[::-1][i+1:])
#    print("\t", n_goods(data[::-1][i+1:]), perms)
#    x = n_goods(data[::-1][i+1:])
#    if x > 1:
#        perms = perms * x
#
#print(10*"=")
#print(perms)

# Løsningen:
permsfor = {
        data[-1] : 1
}
for i, adapter in enumerate(data[::-1][1:]):
    permsfor[adapter] = sum([permsfor.get(adapter+i, 0) for i in range(1, 4)])

print(permsfor)
print(sum([permsfor.get(x, 0) for x in range(1, 4)]))

#print(connect(0, data))

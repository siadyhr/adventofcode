import sys

state = 0
goods = []
data = []
for line in sys.stdin:
    if state == 0:
        if line[:-1]:
            goods.append(tuple(map(int, line.split("-"))))
        else:
            state = 1
    else:
        data.append(int(line[:-1]))

def check_good(value):
    for a, b in goods:
        if a <= value <= b:
            return True
    return False

goods.sort()

new_goods = []
i = 0
while i < len(goods):
    a, b = goods[i]
    j = 1
    while i+j < len(goods) and goods[i+j][0] <= b:
        b = max(b, goods[i+j][1])
        # Max because the new interval could be contained in the old one
        j += 1
    new_goods.append((a, b))
    i += j

print(min(y-x for (x, y) in new_goods))
print(sum(1+y-x for (x, y) in new_goods))

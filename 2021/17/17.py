rawin = input()[13:].split(",")
rawin = [x.strip().split("..") for x in rawin]
print(rawin)
xmin = int(rawin[0][0][2:])
xmax = int(rawin[0][1])

ymin = int(rawin[1][0][2:])
ymax = int(rawin[1][1])

print(xmin, xmax, ymin, ymax)

print("Part 1")
print((abs(ymin) - 1) * abs(ymin)//2)

speeds = []

print("Part 2")
def x_possibilities(turn, xmin, xmax):
    n_vs = 0
    for vx0 in range(0, xmax+1):
        x = 0
        vx = vx0
        for _ in range(turn):
#            print("X-tur: %s -> %s" % (x, x+vx))
            x += vx
            vx = max(0, vx-1)
        if xmin <= x <= xmax:
#            print(x, vx0, turn)
            n_vs += 1
            speeds.append((vx0, vy, turn))

    return n_vs

def will_hit(vy, ymin, ymax):
    y = 0
    turns = 0
    good_turns = []
    while y >= ymin:
        if y <= ymax:
            good_turns.append(turns)
        y += vy
        vy -= 1
        turns += 1
    return good_turns

result = 0
for vy in range(ymin, -ymin):
    good_vys = will_hit(vy, ymin, ymax)
    if good_vys:
        for turn in good_vys:
            n_vxs = x_possibilities(turn, xmin, xmax)
#            print(vy, n_vxs, good_vys)
            result += n_vxs

real_speeds = set((x[0], x[1]) for x in speeds)
for x in sorted(set(speeds)):
    print(x[0], x[1])
print(len(set(speeds)))
print("Result")
print(result)

print("-----")
print(x_possibilities(1, 20, 30))


print("Part 2, final")
print(len(real_speeds))

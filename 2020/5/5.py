import sys

def binpar(data, left, right, N_min, N_max):
    if N_max - N_min == 1:
        return N_max if data[0] == right else N_min
    elif data[0] == left:
        return binpar(data[1:], left, right, N_min, N_max - (N_max + 1 - N_min)//2)
    return binpar(data[1:], left, right, N_min + (N_max + 1 - N_min)//2, N_max)

pass_ids = []
for rawin in sys.stdin:
    rows, seats = rawin[:-4], rawin[-4:]
#    print(rows, seats)
    row = binpar(rows, "F", "B", 0, 127)
    seat = binpar(seats, "L", "R", 0, 7)
#    print(row, seat)
    pass_ids.append(row*8 + seat)

print(max(pass_ids))
pass_ids.sort()
print(pass_ids)
for x, y in zip(pass_ids, pass_ids[1:]):
    if y != x+1:
        print(x+1)
        break


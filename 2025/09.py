#08.00
import sys
data = [tuple(map(int, line[:-1].split(","))) for line in sys.stdin]
areas = {
        (i, j) : (1 + abs(y2 - y1))*(1 + abs(x2 - x1))
        for i, (x1, y1) in enumerate(data)
        for j, (x2, y2) in enumerate(data[i+1:], i+1)
        }

print("Part 1")
print(max(areas.values())) # 08.05

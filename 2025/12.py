# 06.51
import sys
import functools

shapes = []
shape = []
regions = []
for line in sys.stdin:
    if "#" in line or "." in line:
        shape.append(line[:-1])
    if len(line) == 1:
        shapes.append(shape)
        shape = []
    if "x" in line:
        size = list(map(int, line.split()[0][:-1].split("x")))
        to_fill = list(map(int, line.split()[1:]))
        regions.append((size, to_fill))

#print(shapes)
#print(regions)

def area(shape):
    return "".join(shape).count("#")

result = 0
for region, requirements in regions:
    total_area = sum(
            area(shape) * n for shape, n in zip(shapes, requirements)
            )
    if (total_area > region[0] * region[1]):
        continue
    else:
        result += 1
print("Part 1", result) # 07.17

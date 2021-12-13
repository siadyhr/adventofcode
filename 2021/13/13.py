import sys

# Fold in x makes (x+i, y) turn in to (x-i, y)
# Or (x0, y0) to (x - (x0-x), y0) = (2x-x0, y0)
dots = []
folds = []
for line in sys.stdin:
    if not line[:-1]:
        break
    dots.append(tuple(int(x) for x in line[:-1].split(',')))
for line in sys.stdin:
    if "x" in line:
        folds.append(("x", int(line[:-1].split("=")[1])))
    else:
        folds.append(("y", int(line[:-1].split("=")[1])))

def fold(dots, folds):
    for direction, crease in folds:
#        print(direction, crease)
        for i, dot in enumerate(dots):
#            print(dot)
            if direction == "x":
                if dot[0] > crease:
                    dots[i] = (2*crease - dots[i][0], dots[i][1])
                    print("x->", dots[i])
            elif direction == "y":
                if dot[1] > crease:
                    dots[i] = (dots[i][0], 2*crease - dots[i][1])
#                print("y->", dots[i])

def print_dots(dots):
    xmax = max(dot[0] for dot in dots) + 1
    ymax = max(dot[1] for dot in dots) + 1
    print(xmax*"-")
    for y in range(ymax):
        for x in range(xmax):
            print("#" if (x, y) in dots else ".", end="")
        print()
    print(xmax*"-")

print(len([dot for dot in dots if dot[0] > 655]))
            
# part1
#print_dots(dots)
fold(dots, folds[:1])
#print(dots)
print("Hej")
print(set(dots))
print(len(dots))
print(len(set(dots)))
#print_dots(dots)

# part 2
fold(dots, folds[1:])
print(len(set(dots)))
print_dots(dots)

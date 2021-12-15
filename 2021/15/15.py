import sys
from collections import deque

danger = [[int(x) for x in line[:-1]] for line in sys.stdin] 
WIDTH = len(danger[0])
HEIGHT = len(danger)

def get_neighbours(i, j):
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    for di, dj in directions:
        if (
                (0 <= i + di < WIDTH)
                and 
                (0 <= j + dj < HEIGHT)
            ):
            yield (i + di, j + dj)

def explore(i0, j0, danger):
    least_dangerous = [[float('infinity') for _ in range(WIDTH)]
            for __ in range(HEIGHT)]
    least_dangerous[0][0] = 0

    stack = deque()
    stack.append((i0, j0))
    while stack:
        i, j = stack.pop()
#        print("Står i", i, j)
        for neighbour in get_neighbours(i, j):
#            print("Nabo", neighbour)
#            print("Nuværende fare: %s/kommende fare: %s" % (
#                least_dangerous[neighbour[0]][neighbour[1]],
#                least_dangerous[i][j]
#                +
#                danger[neighbour[0]][neighbour[1]]
#                ))
            if least_dangerous[neighbour[0]][neighbour[1]] > (
                    least_dangerous[i][j]
                    +
                    danger[neighbour[0]][neighbour[1]]
                    ):
                least_dangerous[neighbour[0]][neighbour[1]] = (
                    least_dangerous[i][j] + danger[neighbour[0]][neighbour[1]]
                    )
#                print("Læg på stakken, sæt (%s, %s) til %s" % (*neighbour, least_dangerous[neighbour[0]][neighbour[1]]))
                if neighbour != (WIDTH-1, HEIGHT-1):
                    stack.appendleft(neighbour)
#                    stack.extendleft(get_neighbours(*neighbour))
    return least_dangerous

#for line in least_dangerous:
#    print("".join("%4d" % x for x in line))

#print()
#for line in danger:
#    print("".join("%4d" % x for x in line))
print(explore(0, 0, danger)[WIDTH-1][HEIGHT-1])

danger2 = [[0 for _ in range(WIDTH*5)] for __ in range(HEIGHT*5)]
for i in range(HEIGHT*5):
    for j in range(WIDTH*5):
        danger2[i][j] = 1 + (
                danger[i%HEIGHT][j%WIDTH] + i//HEIGHT + j//WIDTH - 1) % 9


WIDTH *= 5
HEIGHT *= 5
print(explore(0, 0, danger2)[WIDTH-1][HEIGHT-1])

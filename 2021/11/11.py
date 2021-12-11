size = 10
def get_neighbours(i, j):
    directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
    for di, dj in directions:
        if (
                (0 <= i + di < size)
                and 
                (0 <= j + dj < size)
            ):
            yield (i + di, j + dj)

def simulate(cave, N):
    n_flashes = 0
    turn = 0
    while turn < N:
        printcave(cave)
        print(turn)
        to_flash = []
        flashed = [[False for _ in range(size)] for __ in range(size)]

        # +1
        for i in range(size):
            for j in range(size):
                cave[i][j] += 1
                if cave[i][j] > 9:
                    to_flash.append((i, j))
        # Flash
#        print(to_flash)
        while to_flash:
#            printcave(cave)
            i, j = to_flash.pop()
            if flashed[i][j]:
                continue
#            print("flash", i, j)
            n_flashes += 1
            flashed[i][j] = True
            for i2, j2 in get_neighbours(i, j):
                cave[i2][j2] += 1
                if not flashed[i2][j2] and cave[i2][j2] > 9:
                    to_flash.append((i2, j2))
        # Reset
        if sum(sum(line) for line in flashed) == size*size and N == float('infinity'):
            return cave, n_flashes, turn+1

        for i in range(size):
            for j in range(size):
                if flashed[i][j]:
                    cave[i][j] = 0
                    flashed[i][j] = False
        turn += 1
    return cave, n_flashes


def printcave(cave):
    for line in cave:
        print("".join(str(x) if x < 10 else "+" for x in line))
    print()

cave = [[int(x) for x in input()] for _ in range(size)]
cave_copy = [[x for x in line] for line in cave]
printcave(cave_copy)
result, n_flashed = simulate(cave_copy, 100)
printcave(result)
print(n_flashed)

cave_copy = [[x for x in line] for line in cave]
result, n_flashed, simultaneous_turn = simulate(cave_copy, float('infinity'))
printcave(result)
print(n_flashed)
print(simultaneous_turn)

def fish_after_days(fishes_in, n_days):
    fishes = [x for x in fishes_in]
    new_fish = 0
    for _ in range(n_days):
        new_fish = fishes[0]
        for i, fish in enumerate(fishes[1:], 1):
            fishes[i-1] = fish
        fishes[8] += new_fish
        fishes[6] += new_fish
    return sum(fishes)

fishes = [0]*(256 + 6)
for x in [int(y) for y in input().split(',')]:
    fishes[x] += 1

print(fish_after_days(fishes, 18))
print(fish_after_days(fishes, 80))
print(fish_after_days(fishes, 256))

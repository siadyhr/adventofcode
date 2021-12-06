n_days = 80
base_length = 6
fishes = [0]*(n_days + base_length)

for x in [int(y) for y in input().split(',')]:
    fishes[x] += 1

new_fish = 0
for _ in range(n_days):
#    print(sum(fishes))
#    print(fishes)
    new_fish = fishes[0]
    for i, fish in enumerate(fishes[1:], 1):
        fishes[i-1] = fish
    fishes[8] += new_fish
    fishes[6] += new_fish

print(fishes)
print(sum(fishes))

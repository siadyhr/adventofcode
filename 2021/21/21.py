import itertools

p1 = int(input().split(":")[1])
p2 = int(input().split(":")[1])

class vec():
    def __init__(self, coords):
        self.coords = coords

    def __repr__(self):
        return "V(" + repr(self.coords) + ")"

    def __iter__(self):
        return iter(self.coords)

    def __add__(self, other):
        return vec([x+y for x,y in zip(self.coords, other.coords)])

def play(positions):
    die = itertools.cycle(iter(range(1, 101)))
    scores = [0] * len(positions)
    player = 0
    n_rolls = 0
    while all(score < 1000 for score in scores):
        result = 0
        for i in range(3):
            n_rolls += 1
            result += next(die)
        positions[player] += result
        positions[player] = (positions[player]-1)%10 + 1
        scores[player] += positions[player]
        player += 1
        player %= len(positions)

    return scores, n_rolls

lookup = {}
# lookup[(positions,), player] gives amount
# of universes each person wins in given this conditions

def play2(positions, scores, player, depth=0):
#    print(depth*">", positions, scores, player)
    if max(scores) >= 21:
#        print(depth*"|", "Win")
#        print(vec([1 if x >= 21 else 0 for x in scores]))
        return vec([1 if x >= 21 else 0 for x in scores])

    if (positions[0], positions[1], scores[0], scores[1], player) in lookup:
        return lookup[(positions[0], positions[1], scores[0], scores[1], player)]

    # else...
    wins = vec([0 for _ in range(len(positions))])
    for rolls in itertools.product([1,2,3], repeat=3):
        new_scores = [x for x in scores]
        new_positions = [x if i != player else (x+sum(rolls)-1)%10 + 1 for i,x in enumerate(positions)]
        new_scores[player] += new_positions[player]

        wins += play2(new_positions, new_scores, (player+1)%2, depth+1)

    lookup[(positions[0], positions[1], scores[0], scores[1], player)] = wins
    return wins

# Part 1
scores, n_rolls = play([p1, p2])
print("Part 1:", min(scores)*n_rolls)

# Part 2
result = play2([p1, p2], [0, 0], 0)
print(result)
print(max(result))

from functools import lru_cache
import sys
from collections import Counter
from time import time

def part1(start, rules):
    return "".join(a + rules.get(a + b, "") for a, b in zip(start, start[1:])) + start[-1]

def part2(start, rules, n):
    result = Counter(start[-1])
    for pair in zip(start, start[1:]):
        result += recursive_polymerization("".join(pair), n)

    return result


@lru_cache()
def recursive_polymerization(pair, n):
    if n == 1:
        return Counter(pair[0] + rules[pair])

    return (
            recursive_polymerization(
                pair[0] + rules[pair],
                n-1)
            +
            recursive_polymerization(
                rules[pair] + pair[1],
                n-1)
            )

def judge(polymer):
    counter = Counter(polymer)
    return max(counter.values()) - min(counter.values())

def judge2(counter):
    return max(counter.values()) - min(counter.values())

initial_polymer = input()
input()

rules = {}
for line in sys.stdin:
    line = line[:-1].split()
    rules[line[0]] = line[2]

polymer = initial_polymer
t0 = time()
for _ in range(10):
    polymer = part1(polymer, rules)
t1 = time()
print(t1-t0)
print(judge(polymer))

print("Part 2")
t0 = time()
counter = part2(initial_polymer, rules, 10)
t1 = time()
print(judge2(counter))
print(t1-t0)

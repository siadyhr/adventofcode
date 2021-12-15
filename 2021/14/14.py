import sys
import collections

def part1(start, rules):
    return "".join(a + rules.get(a + b, "") for a, b in zip(start, start[1:])) + start[-1]

def part2(start, rules):
    pass


def polymerize(start, rules, n, method):
    methods = {
            1 : part1,
            2 : part2
            }
    polymer = start
    for _ in range(n):
        print(_)
        polymer = methods[method](polymer, rules)

    return polymer

def judge(polymer):
    counter = collections.Counter(polymer)
    return max(counter.values()) - min(counter.values())

initial_polymer = input()
input()

rules = {}
for line in sys.stdin:
    line = line[:-1].split()
    rules[line[0]] = line[2]

polymer = polymerize(initial_polymer, rules, 10, 1)
print(judge(polymer))

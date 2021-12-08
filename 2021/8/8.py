import sys

def part1(results):
    return sum(len(result) in (2,4,3,7) for case in results for result in case)
    # 2,4,3,7 is #segments in 1, 4, 7, 8

attempts = []
results = []
for line in sys.stdin:
    raw = line.split('|')
    attempts.append(raw[0].split())
    results.append(raw[1].split())

# part 1
print(part1(results))

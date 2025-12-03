import sys
import functools
data = [
        tuple([int(x) for x in line[:-1]])
        for line in sys.stdin
        ]

def max_joltage(s):
    if len(s) == 2:
        return 10*s[0] + s[1]
    return max(
            10*s[0] + max(s[1:]),
            max_joltage(s[1:])
            )

@functools.cache
def max_joltage2(s, n):
    if n == 1:
        return max(s)
    if len(s) == n:
        return sum(
                x * 10**(n-i-1)
                for i,x in enumerate(s)
                )
    return max(
            10**(n-1) * s[0] + max_joltage2(s[1:], n-1),
            max_joltage2(s[1:], n)
            )

result1 = sum(max_joltage(s) for s in data)
print(result1)

result1 = sum(max_joltage2(s, 2) for s in data)
print(result1)

result2 = sum(max_joltage2(s, 12) for s in data)
print(result2)

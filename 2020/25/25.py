import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/25

pubkeys = []
pubkeys.append(int(input()))
pubkeys.append(int(input()))
print(pubkeys)

def mod_root(results, bases):
    # Find n st. base**n == result (mod 20201227)
    n = 0
    values = [1] * len(bases)
    while True:
        if (n % 100000) == 0:
            print(n//100000)
        for i, (value, base) in enumerate(zip(values, bases)):
            values[i] = (value * base) % 20201227
            if values[i] == results[i]:
                print(values, results)
                return (i, n+1)
        n += 1

secret = mod_root(pubkeys, [7, 7])
print(secret)
key = ( pubkeys[(secret[0]+1)%2] ** secret[1]) % 20201227
print(key)

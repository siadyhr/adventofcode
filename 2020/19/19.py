import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/19

rules = {}
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        number, rest = rawin.split(":")
        if not any([num in rest for num in "0123456789"]):
            rules[int(number)] = rest.strip(' "')
            continue

        rest = [
                [int(num) for num in x.strip().split(" ")]
                for x in rest.strip().split("|")
            ]
        rules[int(number)] = rest
#        print(rawin)
    else:
        break

messages = []
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
    messages.append(rawin)

#print(rules)
#print(messages)

def splits_list(a, b, n):
    # returnér alle strengt voksende n+1-tupler af tal
    # på formen (a, n1, n2, ..., n_(n-1), b)
    if n == 1:
        return [[a, b]]
    return [
        [a] + [x] + y[1:]
        for x in range(a+1, b) for y in splits_list(a+x, b, n-1)
    ]

def splits(a, b, n, depth=0):
#    print((depth+1)*"-", a, b, n)
    if n == 1:
        yield [a, b]
    else:
        for x in range(a+1, b+1-(n-1)):
#            print((depth+1)*">", a, x, b, n)
            for y in splits(x, b, n-1, depth+1):
#                print("|"+(depth+1)*">", a, x, b, n, y)
                yield [a] + y

#def splits(a, b, n):
#    return splits_list(a, b, n)

match_cache = {}
def matches(message, rule_num):
    # Nået til bunden
    if (message, rule_num) in match_cache:
        return match_cache[(message,rule_num)]

    if type(rules[rule_num]) is str:
        match_cache[(message, rule_num)] = True if message == rules[rule_num] else False
        return match_cache[(message,rule_num)]

#    if len(rules[rule_num]) == 1:
#    print("Check '%s' mod %s: %s" % (message, rule_num, rules[rule_num]))
    for branch in rules[rule_num]:
        # Vi skal have (mindst) én branch sand
        # `branch` er bare en liste af subregler
#        print("B:", branch)
        for split in splits(0, len(message), len(branch)):
#            print("Split", [message[split1:split2] for split1, split2 in zip(split, split[1:])])
#            good = True
#            for split1, split2, subrule in zip(split, split[1:], branch):
#                match_cache[(message, rule_num)] = True if matches(message[split1:split2], subrule) else False
#                if not match_cache[(message, rule_num)]:
#                    good = False
#                    break
#            if good:
#                return good
            if all(
                matches(message[split1:split2], subrule)
                for split1, split2, subrule in zip(split, split[1:], branch)
                ):
#                print("OK")
                match_cache[(message, rule_num)] = True
                return True
#    print("Nej")
    match_cache[(message, rule_num)] = False
    return False

does_match = []
for i, message in enumerate(messages):
#    if i<374:
#        continue
    print("%s/%s" % (i+1, len(messages)))
    does_match.append(matches(message, 0))
    print("\t", sum(does_match))
print(messages)
print(sum(does_match))

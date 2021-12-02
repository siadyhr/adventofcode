import sys
import re

# http://adventofcode.com/2020/day/7

rules = dict()
holds = dict()
canbein = dict()
for rawin in sys.stdin:
    rawin = rawin[:-2] # .-, newlinestrip
    print('"' + rawin + '"')
    if rawin:
        if "contain no other bag" in rawin:
            continue
        rawin = rawin.split()
        print(rawin)
        #
        title = " ".join(rawin[:2])
        rule = [
                " ".join(rawin[5+4*i:7+4*i]) for i in range(0, (len(rawin)-4)//4)
                ]
        print(title, rule)
        rules[title] = rule
        #
        for bag in rule:
#            print(bag)
            if not bag in canbein:
                canbein[bag] = []
            canbein[bag].append(title)
#        print(title, rules)
        #
        holds[title] = [
            (int(x), bag) for x, bag in zip(rawin[4::4], rule)
        ]
    else:
        print()

outbags = []
def findcontainers(bag, outerbags):
#    print('o', outerbags)
    candidates = []
    tmpout = []
#    print('cbi', bag, canbein[bag])
    for outbag in canbein[bag]:
        if outbag in outerbags:
            continue
        candidates.append(outbag)
    tmpout += candidates
#    print("c\t", candidates)
    for outbag in candidates:
#        print('ob\t', outbag)
        if outbag not in canbein:
#            print("Y", outbag)
            tmpout.append(outbag)
            continue
        tmpout += findcontainers(outbag, outerbags + tmpout)
    return outerbags + tmpout

outerbags = []
newbags = canbein["shiny gold"]
outerbags += newbags
print(10*"-")
#while newbags:
#    print(10*"*")
#    tmpnewbags = []
#    for bag in newbags:
#        print(bag)
#        if not bag in canbein:
#            if not bag in tmpnewbags and not bag in outerbags:
#                print('c', container)
#                tmpnewbags.append(container)
#        else:
#            for container in canbein[bag]:
#                if not container in tmpnewbags and not container in outerbags:
#                    print('c', container)
#                    tmpnewbags.append(container)
#        outerbags += newbags
#        newbags = tmpnewbags
#
#print(len(set(outerbags)))

def holdsn(bag):
    print(bag)
    if not bag in holds:
        return 1
    print(holds[bag])
    return 1 + sum(
            n * holdsn(subbag) for (n, subbag) in holds[bag]
        )

print(10*"=")
print(holds)
#print(canbein)
print(10*"=")
print(holdsn("shiny gold"))
#print(canbein["shiny gold"])
print(10*"=")
#x = findcontainers("shiny gold", outbags)
#print(findcontainers("shiny gold", outbags))

#print(rules)
#print(canbein)
#print(result)

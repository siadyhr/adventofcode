import sys

def get_wrong_delimiter(string):
    openers = "[({<"

    lookup = {
            "}" : "{",
            ")" : "(",
            "]" : "[",
            ">" : "<",
            }
    
    delimiters = []
    last_opener = ""
    for i, char in enumerate(string):
        if char in openers:
            delimiters.append(last_opener)
            last_opener = char
        elif (lookup[char] == last_opener):
            last_opener = delimiters.pop()
        else:
            return i, char, []
    return -1, "", [last_opener] + [char for char in delimiters[::-1]]

part1 = 0
part2s = []
for line in sys.stdin:
    part1_lookup = {
            "" : 0,
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
            }
    
    part2_lookup = {
            "" : 0,
            "(": 1,
            "[": 2,
            "{": 3,
            "<": 4,
            }
#    print(line[:-1])
#    print("".join(str(x) for x in range(10)))
    wrong_id, wrong_value, closers = get_wrong_delimiter(line[:-1])
    part1 += part1_lookup[wrong_value]
    if wrong_id == -1:
        part2 = 0
        for char in closers:
            if char == "":
                continue
            part2 *= 5
            part2 += part2_lookup[char]
        part2s.append(part2)

print("Part 1:", part1)
part2s.sort()
part2 = part2s[len(part2s)//2]
print("Part 2:", part2)

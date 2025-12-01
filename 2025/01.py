import sys
data = [
        int(line[1:]) if line[0] == "R"
        else
        -int(line[1:])
        for line in sys.stdin
        ]
result = 0
S = 50
for val in data:
    S += val
    S %= 100
    if S == 0:
        result += 1
print("Part 1:", result)

result = 0
S = 50
for val in data:
    S += val
    if S > 0:
        result += S//100
    elif S == 0 and val != 0:
        result += 1
    elif S < 0:
        result += -((S - 1)//100)
        if S == val:
            result -= 1
    S %= 100
print("Part 2:", result)

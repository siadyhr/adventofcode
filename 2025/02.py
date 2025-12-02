data = [
    tuple(map(int, x.split("-")))
    for x in input().split(",")
]
def is_funny(s):
    s = str(s)
    return s[:len(s)//2] == s[len(s)//2:]

def is_funny2(s):
    s = str(s)
    for i in range(1, len(s)//2+1):
        if s == (s[:i] * (len(s)//i)):
            return True
    return False


result = 0
result2 = 0
for start, end in data:
    for x in range(start, end+1):
        if is_funny(x):
#            print(x, "is funny")
            result += x
        if is_funny2(x):
#            print(x, "is funny 2")
            result2 += x
print(result)
print(result2)

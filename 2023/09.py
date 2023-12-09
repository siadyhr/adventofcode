import sys

def extrapolateNext(L):
    for iteration in range(len(L)):
        for i in range(len(L) - iteration - 1):
            L[i] = L[i+1] - L[i]
    return sum(L)

result1 = 0
result2 = 0
for rawIn in sys.stdin:
    parsed = [int(x) for x in rawIn.split(" ")]
    result1 += extrapolateNext([x for x in parsed])
    result2 += extrapolateNext([x for x in parsed[::-1]])

print(result1, result2)

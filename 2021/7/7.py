data = [int(x) for x in input().split(',')]
import statistics

# part 1

median = int(statistics.median(data))
print(sum(abs(x - median) for x in data))

# part 2
def nsum(n):
    return n*(n+1)//2

# cost: ½sum( |xi - a||xi - a + 1| )

average = round(sum(data)/len(data))
print(min(sum(nsum(abs(x - a)) for x in data) for a in range(min(data), max(data))))

import sys

part = 2
if part == 1:
    rows = []
    result = 0
    for line in sys.stdin:
        if line[0] in "+*":
            operations = line[:-1].split()
        else:
            rows.append(list(map(int, line[:-1].split())))

    def prod(it):
        if len(it) == 0:
            return 1
        return it[0] * prod(it[1:])

    for i, operation in enumerate(operations):
        if operation == "+":
            result += sum(row[i] for row in rows)
        else:
            result += prod([row[i] for row in rows])
            
    print(result)
elif part == 2:
    rawdata = [line[:-1] for line in sys.stdin]
    operations = rawdata.pop().split()[::-1]
    def transpose(X):
        Y = []
        for i in range(len(X[0])):
            newline = []
            for line in X:
                newline.append(line[i])
            Y.append(newline)
        return Y

    data = transpose(rawdata)
    data = list("".join(num) for num in data)[::-1]
    print(data)

    i_op = 0
    result = 0
    tmp = 0
    for x in data:
        if not(x.strip()):
            result += tmp
            i_op += 1
            if operations[i_op] == "+":
                tmp = 0
            else:
                tmp = 1
        else:
            if operations[i_op] == "+":
                tmp += int(x)
            else:
                tmp *= int(x)
    result += tmp
    print(result)


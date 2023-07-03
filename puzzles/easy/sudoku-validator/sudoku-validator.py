import sys

# the standard input according to the problem statement.
lineList = []
for i in range(9):
    line = []
    for j in input().split():
        line.append(int(j))
    lineList.append(line)

outText = "true"
for i in range(9):
    for j in range(1, 10):
        if j not in lineList[i]:
            print("Debug1 messages...", file=sys.stderr, flush=True)
            outText = "false"
            break

for i in range(9):
    columnList = []
    for j in range(9):
        if lineList[j][i] in columnList:
            print("Debug2 messages...", file=sys.stderr, flush=True)
            outText = "false"
            break
        else:
            columnList.append(lineList[j][i])

for i in range(3):
    for j in range(3):
        columnList = []
        for m in range(3):
            for n in range(3):
                if lineList[i * 3 + m][j * 3 + n] in columnList:
                    print("i: " + str(i) + " j: " + str(j) + " m: " + str(m) + " n: " + str(n) + " num: " + str(lineList[i * 3 + m][j * 3 + n]) + " columnList: " + " ".join(str(x) for x in columnList), file=sys.stderr, flush=True)
                    outText = "false"
                    break
                else:
                    columnList.append(lineList[i * 3 + m][j * 3 + n])

print(outText)


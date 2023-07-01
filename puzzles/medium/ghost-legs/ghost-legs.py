import sys

# the standard input according to the problem statement.
w, h = [int(i) for i in input().split()]
lineList = []
for i in range(h):
    lineList.append(input())
    print(lineList[i], file=sys.stderr, flush=True)

i = 0
for i in range(w):
    if lineList[0][i] != " ":
        print(lineList[0][i], end = "")
        for j in range(1, h):
            print("j: " + str(j) + " i: " + str(i) + " lineList[j][i]: " + lineList[j][i], file=sys.stderr, flush=True)
            if i > 0:
                if lineList[j][i - 1] == '-':
                    i = i - 3
                    continue
            if i < w - 1:
                if lineList[j][i + 1] == '-':
                    i = i + 3
        print(lineList[h - 1][i], end = "")
        print()

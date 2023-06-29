import sys

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
lineList = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    print(line, file=sys.stderr, flush=True)
    lineList.append(line)

for i in range(height):
    for j in range(width):
        # Three coordinates: a node, its right neighbor, its bottom neighbor
        # The node
        if lineList[i][j] == "0":
            print(j, i, end = " ")
            # Right Node
            for k in range(1, width - j):
                if lineList[i][j + k] == "0":
                    print(j + k, i, end = " ")
                    break
            else:
                print("-1 -1", end = " ")
            # Bottom Node
            for k in range(1, height - i):
                if lineList[i + k][j] == "0":
                    print(j, i + k)
                    break
            else:
                print("-1 -1")

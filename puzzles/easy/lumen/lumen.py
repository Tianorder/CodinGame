import sys

# the standard input according to the problem statement.
n = int(input())
l = int(input())
outList = [[0] * n for i in range(n)]
roomList = []
for i in range(n):
    roomList.append(input().split())
    print(roomList[i], file=sys.stderr, flush=True)

for i in range(n):
    for j in range(len(roomList)):
        if roomList[i][j] == 'C':
            print("i: " + str(i) + " j: " + str(j), file=sys.stderr, flush=True)
            for x in range(i - l + 1, i + l):
                for y in range(j - l + 1, j + l):
                    if x >=0 and x < n and y >= 0 and y < n:
                        print("x: " + str(x) + " y: " + str(y), file=sys.stderr, flush=True)
                        outList[x][y] = 1
output = 0
for i in range(n):
    output += outList[i].count(0)
print(output)


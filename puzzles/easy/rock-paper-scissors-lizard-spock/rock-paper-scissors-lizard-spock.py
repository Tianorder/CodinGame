import sys
import math

def player1Win(numplayer1, signplayer1, numplayer2, signplayer2):
    if signplayer1 == signplayer2:
        return True if numplayer1 < numplayer2 else False
    if signplayer1 == "R":
        return True if signplayer2 in ["L", "C"] else False
    if signplayer1 == "P":
        return True if signplayer2 in ["R", "S"] else False
    if signplayer1 == "C":
        return True if signplayer2 in ["P", "L"] else False
    if signplayer1 == "L":
        return True if signplayer2 in ["S", "P"] else False
    if signplayer1 == "S":
        return True if signplayer2 in ["C", "R"] else False
    

# the standard input according to the problem statement.
winList = []
n = int(input())
for i in range(n):
    inputs = input().split()
    winList.append(inputs)

turnList = []
turn = int(math.log(n, 2))
for i in range(turn):
    # turnList = winList
    turnList = []
    for line in winList:
        turnList.append(line)
    winList = []
    for j in range(n // (2 ** (i + 1))):
        print(str(turnList), file=sys.stderr, flush=True)
        isPlayer1Win = player1Win(int(turnList[j * 2][0]), turnList[j * 2][1], int(turnList[j * 2 + 1][0]), turnList[j * 2 + 1][1])
        if isPlayer1Win:
            turnList[j * 2].append(turnList[j * 2 + 1][0])
            winList.append(turnList[j * 2])
        else:
            turnList[j * 2 + 1].append(turnList[j * 2][0])
            winList.append(turnList[j * 2 + 1])
        print(str(winList), file=sys.stderr, flush=True)


print(winList[0][0])
print(winList[0][2], end = "")
for i in range(turn - 1):
    print(" " + winList[0][i + 3], end = "")
print()


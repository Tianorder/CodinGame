import sys

# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
# 坐标原点
x, y = 0, 0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print(bomb_dir, file=sys.stderr, flush=True)

    if "U" in bomb_dir:
        y0, h = (y0 + y) // 2, y0
    elif "D" in bomb_dir:
        y0, y = (y0 + h) // 2, y0
    if "R" in bomb_dir:
        x0, x = (x0 + w) // 2, x0
    elif "L" in bomb_dir:
        x0, w = (x0 + x) // 2, x0

    # the location of the next window Batman should jump to.
    print(x0, y0)

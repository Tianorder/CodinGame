import sys
# the standard input according to the problem statement.

# game loop
grid = [[True for _ in range(20)] for _ in range(30)]
while True:
    # n: total number of players (2 to 4).
    # p: your player number (0 to 3).
    n, p = [int(i) for i in input().split()]
    for i in range(n):
        # x0: starting X coordinate of lightcycle (or -1)
        # y0: starting Y coordinate of lightcycle (or -1)
        # x1: starting X coordinate of lightcycle (can be the same as X0 if you play before this player)
        # y1: starting Y coordinate of lightcycle (can be the same as Y0 if you play before this player)
        x0, y0, x1, y1 = [int(j) for j in input().split()]
        grid[x0][y0] = False
        grid[x1][y1] = False
        if i == p:
            x = x1
            y = y1

    # A single line with UP, DOWN, LEFT or RIGHT
    # print(grid[x][y + 1], x, y, file=sys.stderr, flush=True)
    if x > 0 and grid[x - 1][y]:
        print("LEFT")
    elif y > 0 and grid[x][y - 1]:
        print("UP")
    elif x < 29 and grid[x + 1][y]:
        print("RIGHT")
    elif y < 19 and grid[x][y + 1]:
        print("DOWN")

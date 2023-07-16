import sys
# the standard input according to the problem statement.

directions = {(0, 1): "DOWN", (0, -1): "UP", (1, 0): "RIGHT", (-1, 0): "LEFT"}


def count_continuous_ones(grid, x, y):
    new_grid = [row[:] for row in grid]
    if new_grid[x][y] != 1:
        return 0

    count = 0
    stack = [(x, y)]
    while stack:
        curr_x, curr_y = stack.pop()
        if new_grid[curr_x][curr_y] == 1:
            count += 1
            new_grid[curr_x][curr_y] = -1

            for direction in directions:
                dx, dy = direction
                new_x = curr_x + dx
                new_y = curr_y + dy

                if 0 <= new_x < 30 and 0 <= new_y < 20 and grid[new_x][new_y] == 1:
                    stack.append((new_x, new_y))

    return count


# game loop
grid = [[1 for _ in range(20)] for _ in range(30)]
while True:
    # n: total number of players (2 to 4).
    # p: your player number (0 to 3).
    n, p = [int(i) for i in input().split()]
    x, y = 0, 0
    for i in range(n):
        # x0: starting X coordinate of lightcycle (or -1)
        # y0: starting Y coordinate of lightcycle (or -1)
        # x1: starting X coordinate of lightcycle (can be the same as X0 if you play before this player)
        # y1: starting Y coordinate of lightcycle (can be the same as Y0 if you play before this player)
        x0, y0, x1, y1 = [int(j) for j in input().split()]
        grid[x0][y0] = 0
        grid[x1][y1] = 0
        if i == p:
            x, y = x1, y1

    direction = ""
    max_count = 0
    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < 30 and 0 <= new_y < 20 and grid[new_x][new_y] == 1:
            count = count_continuous_ones(grid, new_x, new_y)
            print(directions[dx, dy], count, file=sys.stderr, flush=True)
            if count > max_count:
                max_count = count
                direction = directions[dx, dy]
    # A single line with UP, DOWN, LEFT or RIGHT
    print(direction)

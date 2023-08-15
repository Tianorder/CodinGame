# the standard input according to the problem statement.

width, height = [int(i) for i in input().split()]
init_grid = []
for i in range(height):
    line = input()
    init_grid.append(list(line))
turn_grid = list(zip(*init_grid))

new_grid = []
for i, line in enumerate(turn_grid):
    count = line.count("#")
    new_grid.append(["."] * (len(line) - count) + ["#"] * count)

out_grid = list(zip(*new_grid))
for line in out_grid:
    print("".join(line))

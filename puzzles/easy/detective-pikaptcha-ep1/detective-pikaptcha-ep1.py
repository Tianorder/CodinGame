# the standard input according to the problem statement.

width, height = [int(i) for i in input().split()]
line_list = []
for i in range(height):
    line = input()
    line_list.append(line)

out_list = [[0 for _ in range(width)] for _ in range(height)]
for i in range(height):
    for j in range(width):
        # print(out_list, file=sys.stderr)
        if line_list[i][j] == "#":
            out_list[i][j] = -5
        elif line_list[i][j] == "0":
            if i < height - 1:
                out_list[i + 1][j] += 1
            if i > 0:
                out_list[i - 1][j] += 1
            if j < width - 1:
                out_list[i][j + 1] += 1
            if j > 0:
                out_list[i][j - 1] += 1

for out_line in out_list:
    for out in out_line:
        if out < 0:
            print("#", end = "")
        else:
            print(out, end = "")
    print()


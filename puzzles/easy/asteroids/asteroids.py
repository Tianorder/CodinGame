# the standard input according to the problem statement.

w, h, t1, t2, t3 = [int(i) for i in input().split()]
first_dict = {}
second_dict = {}
for i in range(h):
    first_picture_row, second_picture_row = input().split()
    if first_picture_row != "." * w:
        for j, c in enumerate(first_picture_row):
            if c != ".":
                first_dict[c] = (i, j)
    if second_picture_row != "." * w:
        for j, c in enumerate(second_picture_row):
            if c != ".":
                second_dict[c] = (i, j)

out_list = [['.' for _ in range(w)] for _ in range(h)]
asteroids = sorted(first_dict.keys(), reverse=True)
for c in asteroids:
    i = (second_dict[c][0] - first_dict[c][0]) / (t2 - t1) * (t3 - t2) + second_dict[c][0]
    j = (second_dict[c][1] - first_dict[c][1]) / (t2 - t1) * (t3 - t2) + second_dict[c][1]
    if 0 <= i < h and 0 <= j < w:
        i = int(i)
        j = int(j)
        out_list[i][j] = c

for line in out_list:
    for c in line:
        print(c, end="")
    print()

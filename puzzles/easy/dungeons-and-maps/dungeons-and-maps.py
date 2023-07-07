# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
start_row, start_col = [int(i) for i in input().split()]
n = int(input())

# 不存在循环，所以最大值应该是19 * 19，“T”处我没有增加count
min_count = 400
min_map = 0
for i in range(n):
    count = 0
    map_list = []
    for j in range(h):
        map_row = input()
        map_list.append(list(map_row))
    x, y = start_row, start_col
    while map_list[x][y] != "T":
        if map_list[x][y] in ".#":
            break
        elif map_list[x][y] == "^":
            x -= 1
        elif map_list[x][y] == "v":
            x += 1
        elif map_list[x][y] == "<":
            y -= 1
        elif map_list[x][y] == ">":
            y += 1
        count += 1
        if x < 0 or y < 0 or x >= h or y >= w or count > 360:
            break
    else:
        if count < min_count:
            min_count = count
            min_map = i
if min_count == 400:
    print("TRAP")
else:
    print(min_map)

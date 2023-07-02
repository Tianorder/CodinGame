import sys

# the standard input according to the problem statement.
l, c = [int(i) for i in input().split()]
row_list = []
x, y = 0, 0
tele_list = []
for i in range(l):
    row = input()
    row_list.append(row)
    loc = row.find("@")
    if loc != -1:
        x = loc
        y = i
    loc = row.find("T")
    if loc != -1:
        tele_list.extend([loc, i])
if tele_list:
    teleporters = {
        (tele_list[0], tele_list[1]): (tele_list[2], tele_list[3]),
        (tele_list[2], tele_list[3]): (tele_list[0], tele_list[1])
        }

def next_coord(x, y, direction):
    if direction == "SOUTH":
        y +=1
    elif direction == "NORTH":
        y -=1
    elif direction == "WEST":
        x -=1
    elif direction == "EAST":
        x +=1
    return x, y


def next_direction(x, y):
    directions = ["SOUTH", "EAST", "NORTH", "WEST"]
    for i in range(4):
        if is_inverter:
            next_index = (-i - 1) % len(directions)
        else:
            next_index = (i) % len(directions)
        direction = directions[next_index]
        next_x, next_y = next_coord(x, y, direction)
        if row_list[next_y][next_x] not in ("X", "#"):
            return directions[next_index]
        if row_list[next_y][next_x] == "X" and is_breaker:
            row_list[next_y] = row_list[next_y][:next_x] + " " + row_list[next_y][next_x + 1:]
            return directions[next_index]


path = []
direction = "SOUTH"
is_breaker = False
is_inverter = False
is_loop = True
outline_list = []
# 这个鉴定是否loop的方法或许可以设法优化
while (x, y, direction, row_list.copy(), is_breaker) not in path:
    path.append((x, y, direction, row_list.copy(), is_breaker))
    if row_list[y][x] == "$":
        is_loop = False
        break
    elif row_list[y][x] == "T":
        x, y = teleporters[(x, y)]
    elif row_list[y][x] == "S":
        direction = "SOUTH"
    elif row_list[y][x] == "N":
        direction = "NORTH"
    elif row_list[y][x] == "W":
        direction = "WEST"
    elif row_list[y][x] == "E":
        direction = "EAST"
    elif row_list[y][x] == "B":
        is_breaker = not is_breaker
    elif row_list[y][x] == "I":
        is_inverter = not is_inverter

    next_x, next_y = next_coord(x, y, direction)
    if row_list[next_y][next_x] == "#" or (row_list[next_y][next_x] == "X" and not is_breaker):
        direction = next_direction(x, y)
        next_x, next_y = next_coord(x, y, direction)
    elif row_list[next_y][next_x] == "X" and is_breaker:
        row_list[next_y] = row_list[next_y][:next_x] + " " + row_list[next_y][next_x + 1:]

    print(direction, file=sys.stderr, flush=True)
    outline_list.append(direction)
    
    x = next_x
    y = next_y
    # print(path, x, y, file=sys.stderr, flush=True)

if is_loop:
    print("LOOP")
else:
    for outline in outline_list:
        print(outline)


import sys
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
line_list = []
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    line_list.append(line.split())
print(line_list, file=sys.stderr, flush=True)
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).


def exit_direction(typ, pos):
    # if typ in (1, 3, 7, 8, 9, 12, 13):
    #     return "DOWN"
    if pos == "LEFT" and typ in (2, 6):
        return "RIGHT"
    elif pos == "RIGHT" and typ in (2, 6):
        return "LEFT"
    elif pos == "TOP" and typ in (4, 10):
        return "LEFT"
    elif pos == "TOP" and typ in (5, 11):
        return "RIGHT"
    else:
        return "DOWN"


# game loop
# 实际上不需要每轮都计算，但为了Episode 2和3，姑且也每轮计算吧
while True:
    inputs = input().split()
    xi = int(inputs[0])
    yi = int(inputs[1])
    typ = int(line_list[yi][xi])
    pos = inputs[2]
    print(xi, yi, typ, pos, file=sys.stderr, flush=True)
    # 只关心出口方向
    direction = exit_direction(typ, pos)
    if direction == "DOWN":
        yi += 1
    elif direction == "LEFT":
        xi -= 1
    elif direction == "RIGHT":
        xi += 1

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(xi, yi)

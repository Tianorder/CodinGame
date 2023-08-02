import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
image = input()

# 放进二维数组
matrix = [[0 for _ in range(w)] for _ in range(h)]
x = y = 0
codes = image.split(' ')
for i in range(0, len(codes), 2):
    color = codes[i]
    length = int(codes[i + 1])
    if color == 'B':
        fill = 1
    else:
        fill = 0
    x_length = x + length
    next_x = x_length % w
    if x_length > w:
        matrix[y] = matrix[y][:x] + [fill] * (w - x)
        for j in range(x_length // w - 1):
            matrix[y + j + 1] = [fill] * w
        next_y = y + x_length // w
        if next_y != h:
            matrix[next_y] = [fill] * next_x
        y = next_y
    else:
        matrix[y] = matrix[y][:x] + [fill] * (next_x - x) + matrix[y][next_x:]
    x = next_x

note_dict = {}
staff_y_list = [34, 35, 36, 37, 58, 59, 60, 61, 82, 83, 84, 85, 106, 107, 108, 109, 130, 131, 132, 133, 154, 155, 156, 157]


def get_note_by_y(y):
    if 9 < y < 21: # 15
        return "G"
    elif 21 < y < 33: # 27
        return "F"
    elif 33 < y < 45: # 39
        return "E"
    elif 45 < y < 57: # 51
        return "D"
    elif 57 < y < 69:
        return "C"
    elif 69 < y < 81:
        return "B"
    elif 81 < y < 93:
        return "A"
    elif 93 < y < 105:
        return "G"
    elif 105 < y < 117:
        return "F"
    elif 117 < y < 129:
        return "E"
    elif 129 < y < 141:
        return "D"
    elif 141 < y < 153:
        return "C"
    else:
        return " "


def find_note(x, y, matrix):
    # print(x, y, matrix[y][x + 2], file=sys.stderr, flush=True)
    if matrix[y][x + 2] == 1:
        if matrix[y + 2][x + 2] == 0:
            typ = "H"
        else:
            typ = "Q"
        note_dict[x] = get_note_by_y(y) + typ
        for i in range(x - 8, x + 17):
            for j in range(y, h):
                matrix[j][i] = 0
    else:
        for i in range(y, h):
            if matrix[i][x - 2] == 1 and i not in staff_y_list:
                if matrix[i + 4][x - 4] == 0:
                    typ = "H"
                else:
                    typ = "Q"
                note_dict[x] = get_note_by_y(i) + typ
                for i in range(x - 21, x + 2):
                    for j in range(y, h):
                        matrix[j][i] = 0
                break




# 找最上方的点，通过点找音符，在二维数组里删除音符
for i in range(h):
    if i in staff_y_list:
        continue
    while sum(matrix[i]) != 0:
        x = matrix[i].index(1)
        # 找到音符，删除音符
        find_note(x, i, matrix)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

sorted_keys = sorted(note_dict.keys())
out = " ".join(note_dict[key] for key in sorted_keys)
print(out)

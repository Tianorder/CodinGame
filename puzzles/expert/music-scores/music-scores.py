import sys
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
zip_matrix = list(zip(*matrix))


note_string = "GFEDCBAGFEDC"
def get_note_by_y(y):
    print(y, file=sys.stderr, flush=True)
    half_length = note_length / 2
    pure_y = y - (first_one_index - note_length)
    print(pure_y, pure_y / half_length, file=sys.stderr, flush=True)
    return note_string[int(pure_y // half_length)]


# 找五线谱
sum_staff = 0
staff = []
staff_y = []
while zip_matrix:
    row = zip_matrix.pop(0)
    sum_staff = sum(row)
    if sum_staff == 0:
        continue
    else:
        staff = row
        first_one_index = row.index(1)
        first_zero_index = row.index(0, first_one_index)
        next_one_index = row.index(1, first_zero_index)
        note_length = next_one_index - first_one_index
        staff_y = []
        for i in range(6):
            staff_y.extend(list(range(first_one_index + note_length * i, first_zero_index + note_length * i)))
        print(staff_y, file=sys.stderr, flush=True)
        break

sixline_staff = [0] * h
for i in staff_y:
    sixline_staff[i] = 1
previous_row = staff
note_list = []
while zip_matrix:
    row = zip_matrix.pop(0)
    if row != staff and list(row) != sixline_staff:
        if previous_row != staff and list(previous_row) != sixline_staff:
            continue
        else:
            for index, num in enumerate(row):
                if num == 1 and index not in staff_y:
                    y = index
                    break
            else:
                continue
            if zip_matrix[5][y] == 0:
                typ = "H"
            else:
                typ = "Q"
            note_list += [get_note_by_y(y) + typ]
    previous_row = row
print(" ".join(note_list))
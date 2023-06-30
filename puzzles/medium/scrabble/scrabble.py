def calculate_point(letter):
    if letter in "e, a, i, o, n, r, t, l, s, u":
        return 1
    elif letter in "d, g":
        return 2
    elif letter in "b, c, m, p":
        return 3
    elif letter in "f, h, v, w, y":
        return 4
    elif letter in "k":
        return 5
    elif letter in "j, x":
        return 8
    elif letter in "q, z":
        return 10
    else:
        return 0


# the standard input according to the problem statement.
n = int(input())
w_list = []
for i in range(n):
    w = input()
    w_list.append(w)
original_letters = input()
letters = original_letters

max_points = 0
max_w = ""
for w in w_list:
    # 检查w是否符合letters规范
    for ch in w:
        loc = letters.find(ch)
        if loc != -1:
            letters = letters[:loc] + letters[loc + 1:]
        else:
            w = ""
    letters = original_letters
    points = sum(map(calculate_point, w))
    if points > max_points:
        max_points = points
        max_w = w
print(max_w)

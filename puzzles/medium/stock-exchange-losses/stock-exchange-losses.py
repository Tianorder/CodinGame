# the standard input according to the problem statement.

n = int(input())
v_list = []
for i in input().split():
    v = int(i)
    v_list.append(v)

min_diff = 0
max_left_num = max(v_list[: n - 1])
if v_list[n - 1] < v_list[n - 2]:
    diff = v_list[n - 1] - max_left_num
    if diff < min_diff:
        min_diff = diff
for i in range(n - 2, 1, -1):
    if v_list[i - 1] > v_list[i] < v_list[i + 1]:
        diff = v_list[i] - max_left_num
        if diff < min_diff:
            min_diff = diff
    elif v_list[i - 1] < v_list[i] > v_list[i + 1]:
        if v_list[i] == max_left_num:
             max_left_num = max(v_list[: i])
print(min_diff)

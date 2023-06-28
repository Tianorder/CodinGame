# the standard input according to the problem statement.

n = int(input())
v_list = []
e_list = []
for i in range(n):
    v, e = [int(j) for j in input().split()]
    v_list.append(v)
    e_list.append(e)

min_diff = 20000000
for i in range(n):
    for j in range(i + 1, n):
        diff = abs(v_list[i] - v_list[j]) + abs(e_list[i] - e_list[j])
        if diff < min_diff:
            min_diff = diff

print(min_diff)

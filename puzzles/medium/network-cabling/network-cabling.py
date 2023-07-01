# the standard input according to the problem statement.
n = int(input())
x_list = []
y_list = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    x_list.append(x)
    y_list.append(y)
x_list.sort()
sum_x = x_list[-1] - x_list[0]

y_list.sort()
# 我大为震惊，竟然直接取中位数就可以。
# 因为取右边的数那左边所有数要增加，取左边数那右边所有数要增加，需要增加的数量一定大于减少的数量，所以取中位数。
sum_y = sum(abs(y - y_list[n // 2]) for y in y_list)

print(sum_x + sum_y)


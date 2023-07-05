# the standard input according to the problem statement.

n = int(input())
side = n * 2 - 1
out_list = []
# 第一个三角形
for i in range(n):
    out_list.append(" " * (side - i) + "*" * (i * 2 + 1))
# 后两个三角形
for i in range(n):
    out_list.append(" " * (n - i - 1) + "*" * (i * 2 + 1) + " " * (side - i * 2) + "*" * (i * 2 + 1))

out_list[0] = '.' + out_list[0][1:]
for out_line in out_list:
    print(out_line)


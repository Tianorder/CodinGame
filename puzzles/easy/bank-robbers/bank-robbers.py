# the standard input according to the problem statement.
r = int(input())
v = int(input())
time_list = []
for i in range(v):
    c, n = [int(j) for j in input().split()]
    time_list.append(10 ** n * (5 ** (c - n)))

total_time_list = [0] * r
# 每人先干一份工作
for i in range(r):
    if time_list:
        total_time_list[i] += time_list.pop(0)
while time_list:
    min_index = total_time_list.index(min(total_time_list))
    total_time_list[min_index] += time_list.pop(0)

print(max(total_time_list))


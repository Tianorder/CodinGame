import sys

# the standard input according to the problem statement.
l, c, n = [int(i) for i in input().split()]
pi_list = [int(input()) for i in range(n)]

# 一趟能坐所有人的情况
if sum(pi_list) < l:
    print(sum(pi_list) * c)
    exit()

first_group_list = []
money_list = []

total = 0
i = 0
for _ in range(c):
    count = 0
    sum_first_try = 0
    first_group = i % n
    while count <= l:
        count += pi_list[i % n]
        #print("pi和count", pi_list[i % n], count, file=sys.stderr, flush=True)
        i += 1
    i -= 1
    count -= pi_list[i % n]
    total += count
    if first_group in first_group_list:
        break
    else:
        first_group_list.append(first_group)
        money_list.append(count)
else:
    print(total)
    exit()

# 循环的情况
previous_time = first_group_list.index(first_group)
loop_time = len(first_group_list) - previous_time
total = sum(money_list[:previous_time])
total += (c - previous_time) // loop_time * sum(money_list[previous_time:])
final_time = (c - previous_time) % loop_time
total += sum(money_list[previous_time: previous_time + final_time])
print(total)

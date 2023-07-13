import sys

# the standard input according to the problem statement.
n = int(input())
num_list = []
for i in range(n):
    j, d = [int(j) for j in input().split()]
    num_list.append((j, d + j))
num_list.sort()
print(num_list, file=sys.stderr)

i = 0
count = 1
for j in range(1, n):
    if num_list[i][1] <= num_list[j][0]:
        count += 1
        i = j
    elif num_list[i][1] > num_list[j][1]:
        i = j
print(count)

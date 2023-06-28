# the standard input according to the problem statement.

n = int(input())
pi_list = []
for i in range(n):
    pi = int(input())
    pi_list.append(pi)
pi_list.sort()
pi_previous = -9999999
min_diff = 9999999
for pi in pi_list:
    diff = abs(pi - pi_previous)
    if diff < min_diff:
        min_diff = diff
    pi_previous = pi

print(min_diff)

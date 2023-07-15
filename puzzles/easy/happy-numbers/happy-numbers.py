import sys

# the standard input according to the problem statement.
n = int(input())
for i in range(n):
    x = input()
    num = x
    num_list = []
    while num not in num_list:
        print(num, file=sys.stderr, flush=True)
        num_list.append(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    if num == 1:
        print(x, ":)")
    else:
        print(x, ":(")

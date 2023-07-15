import sys

# the standard input according to the problem statement.
r_1 = int(input())
max = (len(str(r_1)) - 1) * 9 + int(str(r_1)[0]) + 1
for i in range(1, max):
    digit = r_1 - i
    while digit < r_1:
        digit = sum([int(j) for j in str(digit)]) + digit
    if digit == r_1:
        print(r_1 - i, file=sys.stderr)
        print("YES")
        break
else:
    print("NO")

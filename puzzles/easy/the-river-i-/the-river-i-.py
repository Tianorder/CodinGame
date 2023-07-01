# the standard input according to the problem statement.
r_1 = int(input())
r_2 = int(input())

while r_1 != r_2:
    if r_1 > r_2:
        r_2 = sum([int(i) for i in str(r_2)]) + r_2
    else:
        r_1 = sum([int(i) for i in str(r_1)]) + r_1
print(r_1)


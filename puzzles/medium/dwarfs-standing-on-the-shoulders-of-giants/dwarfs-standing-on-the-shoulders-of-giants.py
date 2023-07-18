# the standard input according to the problem statement.

n = int(input())  # the number of relationships of influence
xy_list = []
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    xy_list.append([x, y])

max_length = 0
while xy_list:
    xy = xy_list.pop(0)
    if len(xy) > max_length:
        max_length = len(xy)
    for second_xy in xy_list:
        if xy[0] == second_xy[-1]:
            xy_list.append(second_xy[:-1] + xy)
        elif xy[-1] == second_xy[0]:
            xy_list.append(xy[:-1] + second_xy)

# The number of people involved in the longest succession of influences
print(max_length)

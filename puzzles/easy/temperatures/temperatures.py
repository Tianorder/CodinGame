# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
if n == 0:
    print(0)
else:
    min_t = 5527
    list_t = []
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        list_t.append(t)
        abs_t = abs(t)
        if abs_t < min_t:
            min_t = abs_t
    if min_t in list_t:
        print(min_t)
    else:
        print(-min_t)

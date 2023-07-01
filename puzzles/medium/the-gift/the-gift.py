import sys

# the standard input according to the problem statement.
n = int(input())
c = int(input())
b_list = []
for i in range(n):
    b = int(input())
    b_list.append(b)

if sum(b_list) < c:
    print("IMPOSSIBLE")
else:
    b_list.sort()
    length = len(b_list)
    while length:
        # 也可以b = b_list[0]，但在后面的print前要b_list.pop(0)
        b = b_list[-length]
        print(c, length, b, file=sys.stderr, flush=True)
        average = c // length
        if average <= b:
            del_length = length - c % length
            for i in range(del_length):
                print(average)
            c -= average * del_length
            length -= del_length
        else:
            print(b)
            c -= b
            length -= 1

import sys

# the standard input according to the problem statement.
l, h = [int(i) for i in input().split()]
numeral_list = []
for i in range(h):
    numeral = input()
    numeral_list.append(numeral)
str_list = []
for i in range(0, l * 20, l):
    num_str = ""
    for j in range(h):
        num_str += numeral_list[j][i: i + l]
    str_list.append(num_str)

s1 = int(input())
num1_list = []
num1_str = ""
for i in range(s1):
    num1_line = input()
    num1_str += num1_line
    if (i + 1) % h == 0:
        num1_list.append(num1_str)
        num1_str = ""

s2 = int(input())
num2_list = []
num2_str = ""
for i in range(s2):
    num2_line = input()
    num2_str += num2_line
    if (i + 1) % h == 0:
        num2_list.append(num2_str)
        num2_str = ""
operation = input()

num1 = 0
for i in range(len(num1_list)):
    num1 += str_list.index(num1_list[-i - 1]) * (20 ** (i))
num2 = 0
for i in range(len(num2_list)):
    num2 += str_list.index(num2_list[-i - 1]) * (20 ** (i))

num_out = 0
if operation == "+":
    num_out = num1 + num2
elif operation == "-":
    num_out = num1 - num2
elif operation == "*":
    num_out = num1 * num2
elif operation == "/":
    num_out = num1 // num2
print(num_out, file=sys.stderr, flush=True)
if num_out == 0:
    for j in range(l):
        print(str_list[0][j * l: (j + 1) * l])
else:
    num_out_list = []
    while num_out > 0:
        num_out_list.append(num_out % 20)
        num_out = num_out // 20
    print(num_out_list, file=sys.stderr, flush=True)
    for i in range(len(num_out_list) - 1, -1, -1):
        for j in range(l):
            print(str_list[num_out_list[i]][j * l: (j + 1) * l])


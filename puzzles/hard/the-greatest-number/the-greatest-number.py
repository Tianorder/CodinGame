# the standard input according to the problem statement.

n = int(input())
num_list = input().split()
if "-" in num_list:
    num_list.remove("-")
    num_list.sort()
    if "." in num_list:
        num_list.remove(".")
        out_num = "-" + num_list[0] + "." + "".join(num_list[1:])
    else:
        out_num = "-" + "".join(num_list)
else:
    num_list.sort(reverse=True)
    if "." in num_list:
        num_list.remove(".")
        if num_list[-1] == '0':
            out_num = "".join(num_list[:-1])
        else:
            out_num = "".join(num_list[:-1]) + "." + num_list[-1]
    else:
        out_num = "".join(num_list)

if float(out_num) == 0:
    out_num = 0
print(out_num)
# the standard input according to the problem statement.

b = input()
# 评论区用split("0"),然后把相邻的字符串长度相加再加一，再求max，比我的方法好
b = "0" + b + "0"
max_length = 1
loc = 0
next_loc = 0
while next_loc != len(b):
    loc = b.find("0", loc + 1)
    previous_loc = b.rfind("0", 0, loc)
    next_loc = b.find("0", loc + 1)
    if next_loc == -1:
        next_loc = len(b)
    length_one = next_loc - previous_loc - 1
    if length_one > max_length:
        max_length = length_one
print(max_length)


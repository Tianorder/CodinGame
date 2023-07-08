# the standard input according to the problem statement.

# 换算成整数多此一举，Python可以直接比较字符串
n = int(input())
min_time = 86400
min_t = ""
for i in range(n):
    t = input()
    time = int(t[:2]) * 60 * 60 + int(t[3:5]) * 60 + int(t[6:])
    if time < min_time:
        min_time = time 
        min_t = t
print(min_t)

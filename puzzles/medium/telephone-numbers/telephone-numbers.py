# the standard input according to the problem statement.
n = int(input())
tel_list = []
for i in range(n):
    telephone = input()
    tel_list.append(telephone)

# 排序后只要比较相邻两个电话即可
tel_list.sort()
all_count = 0
for i in range(n - 1):
    # count是第一个电话与第二个电话相同的号码数
    count = 0
    length = len(tel_list[i])
    for j in range(length):
        if tel_list[i][j] == tel_list[i + 1][j]:
            count += 1
        else:
            break
    # 用第一个号码的长度减去相同的号码数量，即是第一个号码不重复的号码数量
    all_count += length - count
# 再加上最后一个号码的长度
all_count += len(tel_list[-1])
# The number of elements (referencing a number) stored in the structure.
print(all_count)

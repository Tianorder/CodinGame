# the standard input according to the problem statement.

w, h, count_x, count_y = [int(i) for i in input().split()]
x_list = [int(i) for i in input().split()]
y_list = [int(i) for i in input().split()]
x_list.append(w)
y_list.append(h)

w_list = x_list.copy() + [x_list[i] - x_list[j] for i in range(1, count_x + 1) for j in range(i - 1, -1, -1)]
h_list = y_list.copy() + [y_list[i] - y_list[j] for i in range(1, count_y + 1) for j in range(i - 1, -1, -1)]

# 读别人的代码，他下面只用了句print(sum([h_list.count(i) for i in w_list]))
# ChatGPT说他的代码更好更快，原因如下：
# 1.列表推导式和 sum 函数可以在一行代码中完成相同元素对计数的操作，避免了显式地使用循环和多次查找。
# 2.list.count() 方法在内部实现上可能进行了一些额外的优化，例如使用哈希表来加速查找操作。
# 3.由于我的代码使用了两个指针在已排序的集合上进行遍历，并分别查找对应元素在原始列表中的出现次数，这可能涉及到多次索引操作，而他的代码则直接在原始列表上进行了计数操作。
w_set = sorted(set(w_list))
h_set = sorted(set(h_list))
count = 0
i, j = 0, 0
while i < len(w_set) and j <len(h_set):
    w = w_set[i]
    h = h_set[j]
    if w == h:
        count += w_list.count(w) * h_list.count(h)
        i += 1
        j += 1
    elif w < h:
        i += 1
    elif w > h:
        j += 1

print(count)


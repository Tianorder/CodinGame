import sys

# the standard input according to the problem statement.
l = int(input())
h = int(input())
# 两个字典，一个是area，存储每个O坐标对应的源点，另一个是parent，存储每个源点对应的O坐标。
# 两个判断，如果上和左有一个是O，那parent就跟它一样，没有则parent是自己。如果都是O，则如果父节点一样则一样，不一样则合并父节点
# 合并父节点：把一条父节点上所有值赋给另一个，删除这一个。
area = {}
parent_dict = {}
for i in range(h):
    row = input()
    for j, c in enumerate(list(row)):
        if c == "#":
            area[(j, i)] = []
        elif c == "O":
            water_set = set()
            water_set.add((j, i))
            parent_left = parent_up = tuple()
            if j > 0 and area[(j - 1, i)]:
                parent_left = area[(j - 1, i)]
            if i > 0  and area[(j, i - 1)]:
                parent_up = area[(j, i - 1)]
            if parent_left and parent_up:
                area[(j, i)] = parent_left
                parent_dict[parent_left].append((j, i))
                if parent_left != parent_up:
                    parent_dict[parent_left].extend(parent_dict[parent_up])
                    for node in parent_dict[parent_up]:
                        area[node] = parent_left
                    del parent_dict[parent_up]
            elif parent_left:
                area[(j, i)] = parent_left
                parent_dict[parent_left].append((j, i))
            elif parent_up:
                area[(j, i)] = parent_up
                parent_dict[parent_up].append((j, i))
            else:
                area[(j, i)] = (j, i)
                parent_dict[(j, i)] = [(j, i)]

# print("area", area, file=sys.stderr, flush=True)
# print("parent_dict", parent_dict, file=sys.stderr, flush=True)
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    print(area.get((x, y)), file=sys.stderr, flush=True)
    print(area[(x, y)], file=sys.stderr, flush=True)
    parent = area.get((x, y))
    if parent:
        print(len(parent_dict.get(parent, 0)))
    else:
        print(0)

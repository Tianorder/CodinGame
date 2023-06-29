import sys
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
link_list = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = (int(j) for j in input().split())
    print("n1, n2:", str(n1), str(n2), file=sys.stderr, flush=True)
    link_list.append((n1, n2))
gateway_list = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    print("ei: " + str(ei), file=sys.stderr, flush=True)
    gateway_list.append(ei)

# 寻找最短到达出口的路
def find_shortest_path(start, link_list):
    queue = [(start, [])]
    # 用来筛选已经遍历过的节点
    visited = set()
    while queue:
        print(queue, file=sys.stderr, flush=True)
        node, path = queue.pop(0)
        if node in visited:
            continue

        path.append(node)
        visited.add(node)
        if node in gateway_list:
            return path

        for link in link_list:
            if link[0] == node:
                queue.append((link[1], list(path)))
            if link[1] == node:
                queue.append((link[0], list(path)))

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    print("si: " + str(si), file=sys.stderr, flush=True)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    shortest_path = find_shortest_path(si, link_list)
    if not shortest_path:
        print("error")
        exit()
    print(shortest_path[-2], shortest_path[-1])
    # if (shortest_path[-2], shortest_path[-1]) in link_list:
    #     link_list.remove((shortest_path[-2], shortest_path[-1]))
    # else:
    #     link_list.remove((shortest_path[-1], shortest_path[-2]))

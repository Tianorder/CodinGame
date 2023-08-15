# the standard input according to the problem statement.

w = int(input())
h = int(input())
line_list = []
for i in range(h):
    line = input()
    line_list.append(line)
    
length = h - 1
for i, line in enumerate(line_list):
    if line.startswith("0 1"):
        if ((0 < i < length and line_list[i - 1].startswith("1 1") and line_list[i + 1].startswith("1 1"))
         or (i == 0  and line_list[i + 1].startswith("1 1"))
         or (i == length and line_list[i - 1].startswith("1 1"))):
            print(0, i)
            break
    if line.endswith("1 0"):
        if ((0 < i < length and line_list[i - 1].endswith("1 1") and line_list[i + 1].endswith("1 1"))
         or (i == 0  and line_list[i + 1].endswith("1 1"))
         or (i == length and line_list[i - 1].endswith("1 1"))):
            print(w - 1, i)
            break
    index = 0
    while True:
        index = line.find("1 0 1", index)
        if index == -1:
            break
        if ((0 < i < length and line_list[i - 1][index:index+5] == "1 1 1" and line_list[i + 1][index:index+5] == "1 1 1")
         or (i == 0  and line_list[i + 1][index:index+5] == "1 1 1")
         or (i == length and line_list[i - 1][index:index+5] == "1 1 1")):
            print((index + 2) // 2, i)
            exit()
        index += 4


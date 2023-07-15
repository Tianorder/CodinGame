# the standard input according to the problem statement.

n = int(input())
b_list, c_list = [], []
for i in range(n):
    inputs = input().split()
    b_list.append(inputs[0])
    c_list.append(int(inputs[1]))
s = input()

out = ""
i = 0
while i < len(s):
    for j in range(n):
        k = i + len(b_list[j])
        if s[i:k] == b_list[j]:
            i = k
            out += chr(c_list[j])
            break
    else:
        print("DECODE FAIL AT INDEX", i)
        exit()
print(out)

# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
for i in range(h):
    row = input()
    out = ""
    for ch in t:
        ch_upper = ord(ch.upper())
        if 65 <= ch_upper <= 91:
            loc = ch_upper - 65
        else:
            loc = 26
        out += row[l * loc: l * (loc + 1)]
    print(out)

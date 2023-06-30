import sys

# the standard input according to the problem statement.
r = int(input())
l = int(input())
line = [r]
for i in range(l - 1):
    print(line, file=sys.stderr, flush=True)
    count = 1
    next_line = []
    for i in range(len(line)):
        if i + 1 == len(line):
            next_line.extend([count, line[i]])
            break
        if line[i] == line[i + 1]:
            count += 1
        else:
            next_line.extend([count, line[i]])
            count = 1
    line = next_line.copy()
print(" ".join([str(num) for num in line]))

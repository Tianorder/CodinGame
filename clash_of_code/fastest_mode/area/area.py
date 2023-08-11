import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
o = 0
for i in range(n):
    inputs = input().split()
    shape_type = inputs[0]
    a = int(inputs[1])
    b = int(inputs[2])
    if shape_type == "C":
        o += a * a * math.pi
    else:
        o += a * b


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(round(o, 2))

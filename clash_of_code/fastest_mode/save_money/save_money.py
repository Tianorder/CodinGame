import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
o = b
for i in range(c):
    o += d
    d += 1
o = a - o
if o < 0:
    o = 0
print(o)

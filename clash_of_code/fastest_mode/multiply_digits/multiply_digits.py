import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
time = 0
while len(n) > 1:
    time += 1
    o = 1
    for c in n:
        o = o * int(c)
    n = str(o)
print(time)

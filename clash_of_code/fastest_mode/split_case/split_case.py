import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

o = p = ""
for c in t:
    if ord(c) < 97:
        o += c
    else:
        p += c
print(o)
print(p)
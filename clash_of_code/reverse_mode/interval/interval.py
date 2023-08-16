import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
t = s[::-1]
for i, c in enumerate(s):
    print(c, end="")
    print(t[i], end="")

print()

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
factor = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
o = 1
for i in range(n, 0, -(len(factor))):
    o *= i

print(o)

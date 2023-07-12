import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
a = 1
b = 1
c = 1
for i in range(n - 1):
    c = a + b + 1
    a = b
    b = c

print(c)

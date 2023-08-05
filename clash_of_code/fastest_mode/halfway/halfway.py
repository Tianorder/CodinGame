import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

start = int(input())
end = int(input())
steps = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for i in range(steps):
    start = float(start + end) / 2
print(int(start) + 1)

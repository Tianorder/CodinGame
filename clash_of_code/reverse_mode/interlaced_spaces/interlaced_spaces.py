import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
for i in range(h):
    row = input()
    if i % 2 == 1:
        print(" ", end="")
    print(" ".join([c for c in row]))

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


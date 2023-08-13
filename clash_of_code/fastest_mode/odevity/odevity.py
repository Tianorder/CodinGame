import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

count = int(input())
o = 0
for i in input().split():
    number = int(i)
    if number % 2 == 0:
        o += number
    else:
        o *= number

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(o)

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

digits = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
j = 0
sum = 0
for i in range(10, 1, -1):
    sum += int(digits[j]) * i
    j += 1
if sum % 11 == 1:
    print('X')
elif sum % 11 == 0:
    print("0")
else:
    print(11 - sum % 11)

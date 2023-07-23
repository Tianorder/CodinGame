import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

word = input().lower()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for i in range(len(word) - 1):
    if word[i + 1] < word[i]:
        print(word[i + 1])
        break
else:
    print("True")

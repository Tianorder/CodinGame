import re

# the standard input according to the problem statement.
expression = input()
pattern = r"[^()\[\]{}]"
expression = re.sub(pattern, "", expression)
while expression:
    if "()" not in expression and "[]" not in expression and "{}" not in expression:
        print("false")
        exit()
    expression = expression.replace("()", "").replace("[]", "").replace("{}", "")

print("true")


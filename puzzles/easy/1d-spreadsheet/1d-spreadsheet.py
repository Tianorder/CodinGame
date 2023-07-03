import sys

# the standard input according to the problem statement.
n = int(input())
valueList = [10001] * n
argList = []
for i in range(n):
    argList.append(input().split())
    operation, arg_1, arg_2 = argList[i]
    print(str(operation) + " " + str(arg_1) + " " + str(arg_2), file=sys.stderr, flush=True)
while(True):
    if 10001 not in valueList:
        break
    for i in range(n):
        operation, arg_1, arg_2 = argList[i]
        if arg_1[0] == "$":
            if valueList[int(arg_1[1:])] == 10001:
                continue
            arg_1 = valueList[int(arg_1[1:])]
        if arg_2[0] == "$":
            if valueList[int(arg_2[1:])] == 10001:
                continue
            arg_2 = valueList[int(arg_2[1:])]
        if operation == "VALUE":
            valueList[i] = int(arg_1)
        elif operation == "ADD":
            valueList[i] = int(arg_1) + int(arg_2)
        elif operation == "SUB":
            valueList[i] = int(arg_1) - int(arg_2)
        elif operation == "MULT":
            valueList[i] = int(arg_1) * int(arg_2)
for value in valueList:
    print(value)


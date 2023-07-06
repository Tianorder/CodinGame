# the standard input according to the problem statement.

n = int(input())
m = int(input())
nameList = []
signalList = []
signal_1, signal_2 = "", ""
for i in range(n):
    input_name, input_signal = input().split()
    nameList.append(input_name)
    signalList.append(input_signal)
for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()

    for j in range(n):
        if input_name_1 == nameList[j]:
            signal_1 = signalList[j]
        if input_name_2 == nameList[j]:
            signal_2 = signalList[j]
    
    print(output_name + " ", end = "")
    for j in range(len(signal_1)):
        if _type == "AND":
            if signal_1[j] == "_" or signal_2[j] == "_":
                print("_", end = "")
            else:
                print("-", end = "")
        elif _type == "OR":
            if signal_1[j] == "-" or signal_2[j] == "-":
                print("-", end = "")
            else:
                print("_", end = "")
        elif _type == "XOR":
            if signal_1[j] == signal_2[j]:
                print("_", end = "")
            else:
                print("-", end = "")
        elif _type == "NAND":
            if signal_1[j] == "_" or signal_2[j] == "_":
                print("-", end = "")
            else:
                print("_", end = "")
        elif _type == "NOR":
            if signal_1[j] == "-" or signal_2[j] == "-":
                print("_", end = "")
            else:
                print("-", end = "")
        elif _type == "NXOR":
            if signal_1[j] == signal_2[j]:
                print("-", end = "")
            else:
                print("_", end = "")
    print()


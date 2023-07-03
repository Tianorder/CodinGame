import sys

# the standard input according to the problem statement.
operation = input()
pseudo_random_number = int(input())
print(pseudo_random_number, file=sys.stderr, flush=True)
rotor0 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rotor1 = input()
rotor2 = input()
rotor3 = input()
print(rotor1, file=sys.stderr, flush=True)
print(rotor2, file=sys.stderr, flush=True)
print(rotor3, file=sys.stderr, flush=True)

message = input()
print(message, file=sys.stderr, flush=True)

if operation == "ENCODE":
    for i in range(len(message)):
        # encode1 = chr(ord(message[i]) + pseudo_random_number + i)
        encode1 = rotor0[(rotor0.find(message[i]) + pseudo_random_number + i) % 26]
        encode2 = rotor1[rotor0.find(encode1)]
        encode3 = rotor2[rotor0.find(encode2)]
        encode4 = rotor3[rotor0.find(encode3)]
        print(encode2 + encode3 + encode4, file=sys.stderr, flush=True)
        print(encode4, end = "")
elif operation == "DECODE":
    for i in range(len(message)):
        decode1 = rotor0[rotor3.find(message[i])]
        decode2 = rotor0[rotor2.find(decode1)]
        decode3 = rotor0[rotor1.find(decode2)]
        decode4 = rotor0[(rotor0.find(decode3) - pseudo_random_number - i) % 26]
        print(decode4, end = "")


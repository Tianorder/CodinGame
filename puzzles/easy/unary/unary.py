# the standard input according to the problem statement.

message = input()
message_bin = ""
for ch in message:
    message_bin += bin(ord(ch))[2:].zfill(7)
message_bin += "2"
ch_previous = message_bin[0]
n = 0
out = ""
for ch in message_bin:
    if ch == ch_previous:
        n += 1
    else:
        out += (' 0 'if ch_previous == '1'else' 00 ')+'0'*n
        n = 1
        ch_previous = ch

print(out[1:])

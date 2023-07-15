import sys

# the standard input according to the problem statement.
t = input().split()

out = ""
for para in t:
    i = 0
    for i in range(len(para)):
        if not para[i].isdigit():
            break
    inte = para[:i]
    stri = para[i:]
    print(inte + " " + stri, file=sys.stderr, flush=True)
    ch = ''
    if stri == 'sp':
        ch = ' '
    elif stri == 'bS':
        ch = '\\'
    elif stri == 'sQ':
        ch = "'"
    elif stri == 'nl':
        inte = 1
        ch = '\n'
    else:
        ch = stri
    out = out + int(inte) * ch
print(out)

# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
dict = {}
mt_list = []
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    dict[ext.lower()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    # For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
    if fname.find(".") == -1:
        print("UNKNOWN")
        continue
    ext = fname.split(".")[-1].lower()
    if ext in dict:
        print(dict[fname.split(".")[-1].lower()])
    else:
        print("UNKNOWN")

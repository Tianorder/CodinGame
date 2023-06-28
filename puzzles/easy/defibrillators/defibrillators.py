import math

# the standard input according to the problem statement.

lon = float(input().replace(",","."))
lat = float(input().replace(",","."))
n = int(input())
min_d = 999999999999
out = ""
for i in range(n):
    defib = input()
    info_list = defib.split(";")
    name = info_list[1]
    lonB = float(info_list[4].replace(",","."))
    latB = float(info_list[5].replace(",","."))
    x = (lonB - lon) * math.cos(lat + latB)
    y = latB - lat
    d = math.sqrt(x ** 2 + y ** 2)
    if d < min_d:
        min_d = d
        out = name
print(out)

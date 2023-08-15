# the standard input according to the problem statement.

n, m, c = [int(i) for i in input().split()]
amperes = [int(i) for i in input().split()]
open_appliances = []
sum_amperes = 0
max_sum_amperes = 0
for i in input().split():
    mx = int(i)
    if mx in open_appliances:
        sum_amperes -= amperes[mx - 1]
        open_appliances.remove(mx)
    else:
        sum_amperes += amperes[mx - 1]
        open_appliances.append(mx)
    if sum_amperes > c:
        print("Fuse was blown.")
        exit()
    if sum_amperes > max_sum_amperes:
        max_sum_amperes =sum_amperes

print("Fuse was not blown.")
print("Maximal consumed current was", max_sum_amperes, "A.")

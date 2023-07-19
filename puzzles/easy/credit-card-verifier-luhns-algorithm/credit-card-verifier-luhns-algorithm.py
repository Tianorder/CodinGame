# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    card = input()
    card = card.replace(" ", "")
    num1 = 0
    num2 = 0
    for j in range(len(card) - 2, -1, -2):
        for k in str(int(card[j]) * 2):
            num1 += int(k)
    for j in range(len(card) - 1, 0, -2):
        num2 += int(card[j])
    if (num1 + num2) % 10 == 0:
        print("YES")
    else:
        print("NO")

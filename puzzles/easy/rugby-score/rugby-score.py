# the standard input according to the problem statement.

n = int(input())
for i in range(n // 5 + 1):
    for j in range(i + 1):
        penalty_score = n - i * 5 - j * 2
        if penalty_score < 0:
            break
        if penalty_score % 3 == 0:
            print(i, j, penalty_score // 3)
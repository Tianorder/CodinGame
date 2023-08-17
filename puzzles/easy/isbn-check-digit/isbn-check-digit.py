# the standard input according to the problem statement.

n = int(input())
count = n
invalid_list = []
for i in range(n):
    isbn = input()
    if len(isbn) == 10 and isbn[:-1].isdigit():
        total = sum((10 - index) * int(num) for index, num in enumerate(isbn[:-1]))
        last_num = str(11 - total % 11)
        if last_num == "11":
            last_num = "0"
        if last_num == "10":
            last_num = "X"
        if last_num == isbn[-1]:
               count -= 1
        else:
            invalid_list.append(isbn)
    elif len(isbn) == 13 and isbn[:-1].isdigit():
        total = 0
        for index, num in enumerate(isbn[:-1]):
            num = int(num)
            if index % 2 == 0:
                total += num * 1
            else:
                total += num * 3
        last_num = str(10 - total % 10)
        if last_num == "10":
               last_num = "0"
        if last_num == isbn[-1]:
            count -= 1
        else:
            invalid_list.append(isbn)
    else:
        invalid_list.append(isbn)

print(count, "invalid:")
for invalid in invalid_list:
    print(invalid)

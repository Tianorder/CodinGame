import math

# the standard input according to the problem statement.
n = int(input())
city_list = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    city_list.append((x, y))

first_city = city_list[0]
now_city = city_list[0]
temp_city = (0, 0)
sum_distance = 0
while len(city_list) > 1:
    city_list.remove(now_city)
    min_distance = 9999
    for city in city_list:
        distance = math.sqrt((city[0] - now_city[0]) ** 2 + (city[1] - now_city[1]) ** 2)
        if distance < min_distance:
            min_distance = distance
            temp_city = city
    now_city = temp_city
    sum_distance += min_distance
distance = math.sqrt((first_city[0] - now_city[0]) ** 2 + (first_city[1] - now_city[1]) ** 2)
sum_distance += distance

print(round(sum_distance))

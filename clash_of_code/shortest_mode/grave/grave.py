a=sum(input().count("+")for i in range(int(input())))-4
print(str(0 if a<1 else int(round(100/a,0)))+'%')

x=input()
while x!=x[::-1]:
 x=str(int(x)+int(x[::-1]))
print(x)

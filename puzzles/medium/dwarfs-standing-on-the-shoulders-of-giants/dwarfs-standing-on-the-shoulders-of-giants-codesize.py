a=[[int(j)for j in input().split()]for i in range(int(input()))]
l=[]
while a:
 b=a.pop()
 l+=[len(b)]
 for c in a:
  if b[0]==c[-1]:a+=[c[:-1]+b]
  if b[-1]==c[0]:a+=[b[:-1]+c]
print(max(l))

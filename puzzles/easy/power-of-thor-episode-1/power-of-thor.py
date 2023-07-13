a,b,x,y=map(int,input().split())
while True:
 input()
 o,p="",""
 if b>y:
  o="S"
  y+=1
 elif b<y:
  o="N"
  y-=1
 if a>x:
  p="E"
  x+=1
 elif a<x:
  p="W"
  x-=1
 print(o+p)
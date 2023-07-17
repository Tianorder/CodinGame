a,b,x,y=map(int,input().split())
while 1:
 o=p=""
 if b>y:
  o,y="S",y+1
 elif b<y:
  o,y="N",y-1
 if a>x:
  p,x="E",x+1
 elif a<x:
  p,x="W",x-1
 print(o+p)
 
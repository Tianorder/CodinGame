def a():
 d,e=[],""
 for i in range(int(input())):
  e+=input()
  if(i+1)%h<1:
   d,e=d+[e],""
 return sum(20**i*s.index(d[-i-1])for i in range(len(d)))
def b(i):
 for j in range(l):
  print(s[i][j*l:(j+1)*l])
l,h=map(int,input().split())
t=[input()for _ in range(h)]
s=[''.join(t[j][i:i+l]for j in range(h))for i in range(0,l*20,l)]
x=a()
y=a()
p=input()
o=x*y if p<"+"else x//y if p>"-"else x+y if p<"-"else x-y
if o<1:
 b(0)
else:
 n=[]
 while o>0:
  n,o=n+[o%20],o//20
 [b(n[i])for i in range(len(n)-1,-1,-1)]
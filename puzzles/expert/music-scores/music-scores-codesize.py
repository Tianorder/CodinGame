w,h=map(int,input().split())
m=[[0 for _ in range(w)]for _ in range(h)]
x=y=0
c=input().split()
for i in range(0,len(c),2):
 f=1 if c[i]<'C'else 0
 l=x+int(c[i+1])
 a=l%w
 if l>w:
  m[y]=m[y][:x]+[f]*(w-x)
  for j in range(l//w-1):m[y+j+1]=[f]*w
  y+=l//w
  if y<h:m[y]=[f]*a
 else:m[y]=m[y][:x]+[f]*(a-x)+m[y][a:]
 x=a
z=list(zip(*m))

w="GFEDCBA"*2
while z:
 s=z.pop(0)
 if sum(s)>0:
  a=s.index(1)
  b=s.index(0,a)
  c=s.index(1,b)-a
  v=[j+c*i for i in range(6)for j in range(a,b)]
  break
t=tuple(int(i in v)for i in range(h))
p=s
o=[]
while z:
 r=z.pop(0)
 if r!=s!=t and p in (s,t):
  for i, n in enumerate(r):
   if n>0 and i not in v:
    o+=[w[int((i-a+c)*2//c)]+("H"if z[5][i]<1 else"Q")]
    break
 p=r
print(" ".join(o))
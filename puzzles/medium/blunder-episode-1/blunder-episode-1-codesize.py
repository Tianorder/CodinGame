l,c=map(int,input().split())
r=[]
x=y=0
e=[]
for i in range(l):
 w=input()
 r+=[w]
 j,k=w.find("@"),w.find("T")
 if j>0:x,y=j,i
 if k>0:e+=[(k,i)]
a=["S","E","N","W"]
f=["SOUTH","EAST","NORTH","WEST"]
c=dict(zip(a,f))
def g(x,y,d):
 if d=="S":y+=1
 if d=="N":y-=1
 if d>"V":x-=1
 if d<"F":x+=1
 return x,y
def h(x, y):
 for i in range(4):
  i=(-i-1)%4 if v else i%4
  m,n=g(x,y,a[i])
  z=r[n][m]
  if z not in("X","#")or(z>"W"and b):return a[i]
w=[]
d="S"
b=v=0
p=1
o=[]
while(x,y,d,r.copy(),b)not in w:
 w+=[(x,y,d,r.copy(),b)]
 z=r[y][x]
 if z=="$":
  p=0
  break
 elif z=="T":x,y=e[0]if(x,y)==e[1]else e[1]
 elif z in a:d=z
 elif z=="B":b=1-b
 elif z=="I":v=1-v
 m,n=g(x,y,d)
 z=r[n][m]
 if z=="#"or(z>"W"and 1-b):
  d=h(x,y)
  m,n=g(x,y,d)
 elif z>"W"and b:r[n]=r[n][:m]+" "+r[n][m+1:]
 o+=[c[d]]
 x,y=m,n
if p:o=["LOOP"]
print(*o,sep='\n')

k,v,e,f,n=map(int,input().split()[3:])
d={k:v}
for i in range(n):
 k,v=map(int,input().split())
 d[k]=v
while True:
 k,v,o=input().split()
 k,v=int(k),int(v)
 print('WAIT'if k==-1 or(d[k]>=v and o[0]=='R')or(d[k]<=v and o=='LEFT')else'BLOCK')
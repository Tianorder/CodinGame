n=int(input())
t=[input()for _ in range(n)]
t.sort()
a=0
for i in range(n-1):
 c,l=0,len(t[i])
 for j in range(l):
  if t[i][j]==t[i+1][j]:
   c+=1
  else:
   break
 a+=l-c
a+=len(t[-1])
print(a)

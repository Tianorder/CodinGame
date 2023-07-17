n=int(input())
a=sorted([(j,d+j)for _ in range(n)for j,d in[map(int,input().split())]])
i=0
c=1
for j in range(1,n):
 if a[i][1]<=a[j][0]:c,i=c+1,j
 elif a[i][1]>a[j][1]:i=j
print(c)

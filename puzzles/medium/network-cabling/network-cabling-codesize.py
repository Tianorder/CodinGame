n=int(input())
x,y=zip(*(map(int,input().split())for _ in range(n)))
y=sorted(list(y))
print(max(x)-min(x)+sum(abs(i-y[n//2])for i in y))
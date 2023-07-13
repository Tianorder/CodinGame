w,h,n,a,b=map(int,input().split()+[input()]+input().split())
x,y=0,0
while 1:
 o=input()
 if"U"in o:
  b,h=(b+y)//2,b
 elif"D"in o:
  b,y=(b+h)//2,b
 if"R"in o:
  a,x=(a+w)//2,a
 elif"L"in o:
  a,w=(a+x)//2,a
 print(a,b)

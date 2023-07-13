if input()=='0':
 o=0
else:
 l=list(map(int,input().split()))
 o=min(map(abs,l))
 if o not in l:
  o=-o
print(o)
a=''.join(bin(ord(c))[2:].zfill(7)for c in input())+'2'
b,n,o=a[0],0,''
for c in a:
 if c==b:
  n+=1
 else:
  o,n,b=o+(' 0 'if b=='1'else' 00 ')+'0'*n,1,c
print(o[1:])
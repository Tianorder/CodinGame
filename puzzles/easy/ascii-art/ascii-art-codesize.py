l,h,t=int(input()),int(input()),input()
for i in range(h):
 r,o=input(),''
 for f in t:
  c=b-65 if 64<(b:=ord(f.upper()))<91 else 26
  o+=r[l*c:l*c+l]
 print(o)

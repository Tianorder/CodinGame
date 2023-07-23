d=dict(zip([chr(i+65)for i in range(26)],['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']))
l=input()
z=["".join(d[c]for c in input())for _ in range(int(input()))]
a=len(l)
p=[0]*(a+1)
p[0]=1
for i in range(a):
 if p[i]:
  for w in z:
   if l[i:i+len(w)]==w:p[i+len(w)]+=p[i]
print(p[-1])

n=int(input())
ansa=[]
ansb=[]
final=[]
st=1
ansa.append(st)
s=1
ansb.append(s)

for i in range((n//2)-1):
    st*=2
    ansa.append(st)

for i in range((n//2)-1):
    s*=3
    ansb.append(s)
    
for i in range(n//2):
    final.append(ansa[i])
    final.append(ansb[i])
print(final[n-1])

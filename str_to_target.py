s=input()
t=input()
ans=0
new=0
k=2
if len(t)<len(s):
    print("NO")
else:
    for i in range(len(s)):
        if s[i]!=t[i]:
            new=i
            ans+=len(s)-i
            break
ans+=len(t)-new
if ans<=k:
    print("YES")
else:
    print("NO")
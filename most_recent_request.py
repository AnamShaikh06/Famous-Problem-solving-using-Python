# starting from the right we need to find most recent request and eliminate the repeated once and consider it only once
a=list(map(str,input().split()))
ans=[]
for i in range(len(a)-1,-1,-1):
    if a[i] in ans:
        continue
    else:
        ans.append(a[i])
        
print(ans)
# displaying maximum from the window size in continuous way
arr=[1,3,-1,-3,5,3,6,7]
k=3
ans=[]
for i in range(len(arr)-k+1):
    window=arr[i:i+k]
    ans.append(max(window))
print(ans)
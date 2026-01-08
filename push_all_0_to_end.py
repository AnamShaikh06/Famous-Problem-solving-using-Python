#To push all 0 in array to end
arr=[0,5,0,7,9,0,1,0,2,8,0,4,0]
c=0
for i in range(len(arr)):
    if arr[i]==0:
        arr.remove(arr[i])
        arr.insert(len(arr),0)
print(arr)
# odd even transform works on array where it occurs n times size of array
# also if it is odd integer than +3 and even integer -3

arr=[3,4,9]
for i in range(len(arr)):
    if arr[i]%2!=0:
        arr[i]+=3
    else:
        arr[i]-=3
print(arr)
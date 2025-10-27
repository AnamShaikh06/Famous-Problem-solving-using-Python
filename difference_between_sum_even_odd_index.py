#sum of even and odd index element from 0 to n index and their difference
arr=[1,2,3,4,5]
es=os=0
for i in range(len(arr)):
    if i%2==0:
        es+=arr[i]
    else:
        os+=arr[i]

print(abs(es-os))
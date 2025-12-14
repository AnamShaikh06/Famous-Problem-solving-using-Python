# find sum of unique elements in the array
arr=[1,3,2,3,2,4]
new=[]
for  i in arr:
    if i not in new:
        new.append(i)
        
print(sum(new))
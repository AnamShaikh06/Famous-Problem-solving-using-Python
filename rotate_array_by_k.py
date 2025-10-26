#to rotate an array by k=2
a=[1,3,6,9,10]
k=2
# print(a[k:]+a[:k]) using slicing  

#using for loop
for i in range(k):
    s=a.pop(0)
    a.append(s)
print(a)
    

#to move the zeroes to the end of the array 
a=[1,2,0,9,0,0,6,3,0,7,0,1,0,5]
idx=c=0
for i in range(len(a)):
    if a[i]!=0:
        a[idx]=a[i]
        idx+=1
for i in range(idx,len(a)):
    a[i]=0
print(a)
# perfect number: the addition of all its factors gives ans
#as that number

num=6
sum=0
for i in range(1,num//2+1):
    if num%i==0:
        sum+=i
if sum==num:
    print("Perfect number")
else:
    print("Not a perfect number")
#to sum the prime digits in number
def primecheck(n):
    prime=True
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
    return prime       
num=235637
sum=0
new=str(num)
for i in range(len(new)):
    
    if primecheck(int(new[i])):
        sum+=int(new[i])

print(sum)
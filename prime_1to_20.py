#to print prime numbers from 1 to 20
ans=[]

for i in range(2,21):
    prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            prime=False
            break
    else:
        ans.append(i)
print(ans)
            
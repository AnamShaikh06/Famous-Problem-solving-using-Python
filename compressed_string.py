# compress the string correctly in alphabetical order
a="a3b2c5a1g9c2"

ans=""
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i].isalpha():
            if a[i]==a[j]:
                ans+=a[i]
                ans+=str(int(a[i+1])+int(a[j+1]))
    else:
        if a[i] not in ans:
            if a[i].isalpha():
                ans+=a[i]
                ans+=a[i+1]    
print(ans)
            
        
n=input()[::-1]
num=""
ans=""
for i in range(len(n)):
    num+=n[i]
    if num=="32":
       ans+=" " 
       num=""
    elif num.isdigit() and 65<=int(num)<=122:
        ans+=chr(int(num))
        num=""   
    
print(ans)
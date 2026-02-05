#do the following 
#1010->+  1011->-   1100->*   1101->/
# and digits from 0 to 9
n=input()
li={'1010':'+','1011':'-','1100':'*','1101':'/'}
ans=[]
new=""
if len(n)==4 and int(n,2)<=9:
    print(int(n,2))
else:
    while(len(n)%4!=0):
        n='0'+n

    for i in range(0,len(n),4):
        ans.append(n[i:i+4])

    for i in range(len(ans)):
        if ans[i] in li:
            new+=li[ans[i]]
        else:
            new+=str(int(ans[i],2))
    
print(new)
    
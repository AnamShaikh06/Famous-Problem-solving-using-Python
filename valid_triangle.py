toy=['221','333','345','113']
ans=[]
for i in range(len(toy)):
    a=int(toy[i][0])
    b=int(toy[i][1])
    c=int(toy[i][2])

    if a+b>c:
        if a==b:
            if b==c:
                ans.append("Equilateral")
            else:
                ans.append("Isoceles")
        else:
            ans.append("None of these")
    else:
        ans.append("Not valid")
        
print(ans)
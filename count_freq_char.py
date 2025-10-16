a=input("Enter a string :").lower()
freq={}
for i in a :
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

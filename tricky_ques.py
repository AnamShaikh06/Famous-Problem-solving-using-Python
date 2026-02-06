# find first vowel
# move all the letter begor vowel to end 
# add "ay" to end 
st=input("Enter a string: ")
vow={'a','e','i','o','u'}
new=""
for i in range(len(st)):
    if st[i] in vow:
        new=st[i:]+st[:i]+"ay"
        break
print(new)
        
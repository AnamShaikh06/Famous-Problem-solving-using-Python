#to reverse each word in a string that are separated with space

s=input("Enter the string separated with spaces").split()
for i in range(len(s)):
    s[i]=s[i][::-1]
a=" ".join(s)
print(a)
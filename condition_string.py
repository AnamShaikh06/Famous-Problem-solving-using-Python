#print the first five letters of the string if the len of two string is greater than 12
a=list((input("Enter two strings separated by space:").split()))
new="".join(a)
if len(new)>12:
    print(new[:5])
else:
    print("Length is small ")
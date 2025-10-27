#Must contain uppercase, lowercase, digit, special char, min 8 length
st=input("Enter the password: ")
up=False
low=False
dig=False
special=False
if len(st)>=8:
    for i in st:
        if i.isalnum():
            if i.isdigit():
                dig=True
            if i.isupper():
                up=True
            if i.islower():
                low=True
        else:
            special=True
            
    if up and low and special and dig:
        print("Valid password")
    else:
        print("Not a valid password")
else:
    print("Enter a 8 digit password")
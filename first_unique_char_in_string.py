#to identify the first unique character in the string
s="Anam".lower()
for ch in s:
    if s.count(ch)==1:
        print(ch)
        break
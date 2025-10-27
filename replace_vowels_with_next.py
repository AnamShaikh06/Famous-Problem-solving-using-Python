vow={'a','e','i','o','u'}
s='infosys'
for i in s:
    if i in vow:
        s=s.replace(i,chr(ord(i)+1))
print(s)
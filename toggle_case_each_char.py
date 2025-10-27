#toggle case for each character means upper to lower and lower to upper
st="AnAm is GOod in StuDies"
res=""
for i in st:
    if i.isupper():
        res+=i.lower()
    else:
        res+=i.upper()
print(res)
print(st.swapcase)
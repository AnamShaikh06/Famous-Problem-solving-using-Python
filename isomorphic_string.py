s=input()
t=input()
if len(set(zip(s,t)))==len(set(s))==len(set(t)):
    print("Isomorphic")
else:
    print("Not Isomorphic")
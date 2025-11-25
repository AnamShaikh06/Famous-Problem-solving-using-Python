#to implement the genetic algorithm for the crossover of two genes
import random
target="HELLO"
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s=""
for i in target:
    s+=random.choice(chars)

while s!=target:
    print(s)
    new=list(s)
    for i ,c in enumerate(new):
        if c!=target[i]:
            new[i]=random.choice(chars)
    s="".join(new)

print("Target found",s)
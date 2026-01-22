product=['eggs','milk','cheese']
cp=[2.89,3.29,5.79]

cpmap=dict(zip(product,cp))

product_sold=['eggs','eggs','cheese','milk']
sp=[2.89,2.99,5.97,3.29]

count=0
for prod,sell in zip(product_sold,sp) :
    if sell!=cpmap[prod]:
        count+=1
print(count)
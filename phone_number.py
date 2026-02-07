s=input("Tell me a phone number: ")
dic={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5',
     'six':'6','seven':'7','eight':'8','nine':'9'}
li=s.split()
new=''
num=''
for i in range(len(li)-1,-1,-1):
    if li[i]=='double':
        new+=num
    if li[i]=='triple':
        new+=num
        new+=num
    if li[i] in dic:
        new+=dic[li[i]]
        num=dic[li[i]]
        
print(new[::-1])
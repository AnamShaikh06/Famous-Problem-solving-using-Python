#To find the absolute difference of the square matrix means both diagonal elements sum and 
# then their difference .
n=int(input("Enter the size:"))
mat=[]
for i in range(n):
        mat.append(list(map(int,input().split())))
d1=0
d2=0
for i in range(len(mat)):
    d1+=mat[i][i]
    d2+=mat[i][n-i-1]
print(abs(d1-d2))
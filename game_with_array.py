#The values in arr[] are obtained by doing Xor of consecutive elements in the array.
#User function Template for python3

def game_with_number (arr,  n) : 
    for i in range(n):
        if i!=n-1:
            arr[i]= arr[i]^arr[i+1]
        else:
            arr[i]=arr[i]
    return arr

print(game_with_number([10,11,1,2,3],5))
        
        
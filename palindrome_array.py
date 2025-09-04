#whether the array is palindrome or not
# Function should return true/false
def isPalinArray(arr):
    
    for i in range(len(arr)):
        if str(arr[i])==str(arr[i])[::-1]:
            arr[i]=True
        else:
            return False
 
    return arr

print(isPalinArray([111,222,333,454,777]))
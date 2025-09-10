#Given an array arr[] containing positive elements. A and B are two numbers defining a range. The task is to check if the array contains all elements in the given range (inclusive).

class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        a=set(arr)
        for i in range(A,B+1):
            if i not in arr:
                    return False
        return True

s=Solution()
print(s.check_elements([1,4,5,2,7,8,3],7,2,9))
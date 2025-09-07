#Given an array of arr[] positive integers where all numbers occur even number of times except one number which occurs odd number of times. Return that number.
class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        result = 0
        for num in arr:
            result ^= num
        return result
            
       
s=Solution()
print(s.getOddOccurrence([1,2,2,2,2,3,5,5,5,5,5,9,7]))
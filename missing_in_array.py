#You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. 
# Your task is to identify and return the missing element.
class Solution:
    def missingNum(self, arr):
        n=len(arr)+2
        r=[*range(1,n)]
        s=set(arr)
        for i in r:
            if i not in s:
                return i
              
s=Solution()
print(s.missingNum([1,3,4,5,6]))  
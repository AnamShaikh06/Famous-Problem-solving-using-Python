#Given two sorted arrays arr1 and arr2 of distinct elements. 
# Given a value x. The problem is to count all pairs from both arrays whose sum equals x.
class Solution:
    def countPairs(self,arr1, arr2, x):
        arr1.sort()
        arr2.sort()
        c=0
        i=0
        j=len(arr2)-1
        while i<len(arr1) and j>=0:
            s=arr1[i]+arr2[j]
            if s==x:
                c+=1
                i+=1
                j-=1
            elif s<x:
                i+=1
            else:
                j-=1
        return c
s=Solution()
print(s.countPairs([1,2,5,4],[2,6,8,7],8))
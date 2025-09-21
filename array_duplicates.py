#Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, return an array of all the integers that appears twice.
# Note: You can return the elements in any order but the driver code will print them in sorted order.
class Solution:
    def findDuplicates(self, arr):
        frq={}
        for i in arr:
            if i in frq:
                frq[i]=frq[i]+1
            else:
                frq[i]=1
        lst=[]
        for key,val in frq.items():
            if val>=2:
                lst.append(key)
        return lst

s=Solution()
print(s.findDuplicates([1,2,2,5,6,5,7,7,7,9]))
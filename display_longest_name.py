#Given an array arr[] containing strings of names. Your task is to return the longest string. If there are multiple names of the longest size, return the first occurring name.
class Solution:
    def longest(self, arr):
        l=0
        for i in arr:
            l=max(l,len(i))
        for i in range(len(arr)):
            if l==len(arr[i]):
                return arr[i]
s=Solution()
print(s.longest(["Apple", "Mango", "Orange", "Banana"]))
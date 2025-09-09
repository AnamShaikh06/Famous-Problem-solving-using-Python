#Given an array arr[], swap the kth element from the beginning with the kth element from the end.
# Note: 1-based indexing is followed.


class Solution:
    def swapKth(self, arr, k):
        arr[k-1],arr[-k]=arr[-k],arr[k-1]
        return arr
            
s=Solution()
print(s.swapKth([1,6,8,4,-1,7,9],3))        

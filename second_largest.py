#Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
# Note: The second largest element should not be equal to the largest element.
class Solution:
    def getSecondLargest(self, arr):
        new=list(set(arr))
        new.sort()
        if len(new)<=1:
            return -1
        else:
            return new[-2]
        
s=Solution()
print(s.getSecondLargest([1,8,6,7,9,2,4]))
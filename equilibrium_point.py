#Given an array of integers arr[], the task is to find the first equilibrium point in the array.
# The equilibrium point in an array is an index (0-based indexing) such that the sum of all
# elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. 
# User function Template for python3

class Solution:
    def findEquilibrium(self, arr):
        total_sum = sum(arr)     # total of all elements
        l_sum = 0
        for i in range(len(arr)):
            # r_sum can be derived instead of recalculating
            r_sum = total_sum - l_sum - arr[i]
            if l_sum == r_sum:
                return i   
            # update l_sum for next step
            l_sum += arr[i]
        return -1
s=Solution()
print(s.findEquilibrium([4,2,1,5,1]))
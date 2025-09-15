#An array is balanced if the sum of left half is equal to the right half.

class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        n=len(arr)
        arr[:]=[sum(arr[0:n//2])]+[sum(arr[n//2:n])]
        return abs(arr[1]-arr[0])
#left half will have 1 element less than right half if array is odd size
s=Solution()
print(s.min_value_to_balance([1,2,5,1,7,6,3]))
#Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, 
# find both the duplicate number and the missing number.
class Solution:
    def findTwoElement(self, arr):
        n = len(arr)   
        ans = []
        freq = {}

        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

      
        for key, val in freq.items():
            if val >= 2:
                ans.append(key)

        # find missing element
        for i in range(1, n+1):
            if i not in freq:   # O(1) lookup instead of scanning arr
                ans.append(i)
                break   # only one missing

        return ans

s=Solution()
print(s.findTwoElement([1,5,5,8,9,2,7,3,6]))
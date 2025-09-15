#First sort the array then find whether three numbers are such that the sum of two elements equals the third element.
class Solution:
    def findTriplet(self, arr):
        n = len(arr)
        arr.sort()

        for k in range(n):   
            for i in range(k):       
                for j in range(i+1, k): 
                    if arr[i] + arr[j] == arr[k]:
                        return True
        return False

s=Solution()
# print(s.findTriplet([1,2,7,6]))
print(s.findTriplet([1,2,9,6]))
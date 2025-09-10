#Given an array, arr[] of positive elements, and an integer k, the task is to left-rotate the array k indexes.
# Note: Rotate the array even if the k is greater than the size of the array. 
# arr[] = [1, 2, 3, 4, 5, 6],  k = 11
# [6, 1, 2, 3, 4, 5] as output

class Solution:
    def leftRotate(self, arr, k):
        n=len(arr)
        if k<len(arr):
            arr[:]=arr[k:]+arr[0:k]
            return arr
        else:
            if k%n==0:
                return arr
            else:
                arr[:]=arr[(k%n):]+arr[0:(k%n)]
                return arr
s=Solution()
print(s.leftRotate([1,2,3,4,5,6],11))
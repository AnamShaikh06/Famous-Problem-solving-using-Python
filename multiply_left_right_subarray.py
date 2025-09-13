#You are given an array of integers, your task is to divide the array into two sub-arrays (left and right) containing half of the array elements. Find the sum of the subarrays and then return the multiply of both the subarrays.

#User function Template for python3

class Solution:
    def multiply(self, arr):
        p=1
        if len(arr)%2 ==0:
            arr[:]=[sum(arr[0:len(arr)//2])]+[sum(arr[len(arr)//2 :len(arr)])]
            for i in range(len(arr)):
                p*=arr[i]
            return p
        else:
            arr[:]=[sum(arr[0:len(arr)//2])]+[sum(arr[len(arr)//2 :len(arr)])]
            for i in range(len(arr)):
                p*=arr[i]
            return p
s=Solution()
print(s.multiply([1,2,3,4]))
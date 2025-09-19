#find the maximum product of two numbers in an array
class Solution:
	def maxProduct(self,arr):
		arr.sort()
		return arr[-1]*arr[-2]
s=Solution()
print(s.maxProduct([1,5,6,2,3,9,9,8,7]))
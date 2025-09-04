#to calculate the sum of an array

class Solution:
	def arraySum(self, arr):
   		
   		sum=0
   		for i in arr:
   		    sum+=i
   		return sum

s=Solution()
print(s.arraySum([1,2,3,4]))
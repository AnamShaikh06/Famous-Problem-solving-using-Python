#If the next element is smaller, update the current index to that element. If not, then update to -1.
class Solution:
	def immediateSmaller(self, arr):
		
		for i in range(len(arr)):
		    if i==len(arr)-1:
		        arr[i]=-1
		    elif arr[i]>arr[i+1]:
		        arr[i]=arr[i+1]
		    else:
		        arr[i]=-1
		return arr

s=Solution()
print(s.immediateSmaller([5,6,2,3,1,7]))
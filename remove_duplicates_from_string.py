#Removing duplicates and printing it only once
class Solution:
	def removeDuplicates(self, s):
	    new=""
	    for i in s:
	        if i not in new:
	            new+=i
	    return new
s=Solution()
print(s.removeDuplicates("AnamaShaikh"))
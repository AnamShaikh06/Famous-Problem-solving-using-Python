#print alternates starts from 0

class Solution:
    def getAlternates(self, arr):
        
        return arr[::2]
    
s=Solution()
print(s.getAlternates([10,20,30,50,90,100]))
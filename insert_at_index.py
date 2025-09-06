#insert the given element at particular index
class Solution:
    def insertAtIndex(self, arr, index, val):
        arr.insert(index,val)
        return arr
    
s=Solution()
print(s.insertAtIndex([1,2,5,6,7,90],2,8))

#You are given two arrays a[] and b[], return the Union of both the arrays in any order.
# The Union of two arrays is a collection of all distinct elements present in either of the arrays.
class Solution:    
    def findUnion(self, a, b):
        new=[]
        a=list(set(a))
        b=list(set(b))
        for i in a:
            new.append(i)
        for i in b:
            new.append(i)
        new=list(set(new))
        return new
s=Solution()
print(s.findUnion([1,5,6,7,7,8,2,4,5,6],[7,6,10,8,2]))
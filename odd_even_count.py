#count the odd and even number of elements in an array

class Solution:
    def countOddEven(self, arr):
        e=0
        o=0
        for i in arr:
            if i%2==0:
                e+=1
            else:
                o+=1
        return o,e

s=Solution()
print(s.countOddEven([10,15,9,6,2,4,3]))
# Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.
# Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        freqa={}
        freqb={}
        for i in a:
            if i in freqa:
                freqa[i]+=1
            else:
                freqa[i]=1
        for i in b:
            if i in freqb:
                freqb[i]+=1
            else:
                freqb[i]=1
        return freqa==freqb
s=Solution()
print(s.checkEqual([4,5,8,7,4,8,9],[9,7,8,4,5,8,4]))
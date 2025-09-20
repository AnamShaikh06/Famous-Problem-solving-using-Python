#Given an array of elements occurring in multiples of k, except one element which doesn't occur in multiple of k. Return the unique element.

class Solution:
    def find_unique(self, k, arr):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for key,val in freq.items():
            if val==1:
                return key
s=Solution()
print(s.find_unique(4,[2,2,2,1,2,7,3,7,7,7,3,3,3]))         
            
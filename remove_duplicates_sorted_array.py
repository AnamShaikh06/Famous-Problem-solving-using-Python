# You are given a sorted array arr[] containing positive integers.
# Your task is to remove all duplicate elements from this array such that each element appears only once.
class Solution:
    def removeDuplicates(self, arr): 
        freq={}
        new=[]
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for key,val in freq.items():
            new.append(key)
        return new
s=Solution()
print(s.removeDuplicates([1,2,4,4,2,8,9,6,3,6,3]))
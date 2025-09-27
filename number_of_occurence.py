#Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 
class Solution:
    def countFreq(self, arr, target):
        # code here
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for key,val in freq.items():
            if key==target:
                return val
        return 0

s=Solution()
print(s.countFreq([1,2,5,8,6,2,7,2,7,2],7))
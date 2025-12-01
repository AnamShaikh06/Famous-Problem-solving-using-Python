from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        return len(set(freq.values()))==len(freq.values())
s=Solution()
print(s.uniqueOccurrences([1,1,2,5,1,2,3,2,5]))
print(s.uniqueOccurrences([1,1,2,5,1,5]))
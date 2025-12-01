from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1l=s1.split()
        s2l=s2.split()
        
        ans=[]
        for i in s1l:
            if s1l.count(i)==1 and i not in s2l:
                ans.append(i)
        for i in s2l:
            if s2l.count(i)==1 and i not in s1l:
                ans.append(i)
        return ans
    
s=Solution()
print(s.uncommonFromSentences("this is an apple apple","this is a banana"))

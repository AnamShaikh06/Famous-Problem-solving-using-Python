# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.
class Solution:
    def maxFreqSum(self, s: str) -> int:
        freqv={}
        freqc={}
        l={'a','e','i','o','u'}
        for i in s:
            if i in l:
                if i in freqv:
                    freqv[i]+=1
                else:
                    freqv[i]=1
            else:
                if i in freqc:
                    freqc[i]+=1
                else:
                    freqc[i]=1

        if freqv:
            mv=max(freqv.values())
        else:
            mv=0
        if freqc:
            mc=max(freqc.values())
        else:
            mc=0
        return mv+mc
            
s=Solution()
print(s.maxFreqSum("successses"))
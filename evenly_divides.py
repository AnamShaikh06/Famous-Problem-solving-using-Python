#to find how many digit in a number divide that number completely

class Solution:
    def evenlyDivides(self, n):
        a=str(n)
        c=0
        for i in a:
            if i !='0':
                if n%int(i)==0:
                    c+=1         
        return c
s=Solution()
print(s.evenlyDivides(64))
# Replace all the zeros with 5 in an array
class Solution:
    def convertFive(self, n):
        a=[]
        for i in range(len(str(n))):
            r=n%10
            if r==0:
                a.append(5)
            
            else:
                a.append(r)
            n=n//10
        a.reverse()
        c=0
        for digit in a:
            c = c * 10 + digit
        return c
    
s=Solution()
print(s.convertFive(2050920))
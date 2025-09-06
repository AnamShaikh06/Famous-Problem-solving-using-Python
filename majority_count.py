#Given an array arr[] and two elements x and y, return the element that occurs more frequently. If both elements have the same frequency, return the smaller one.
class Solution:
    def moreFrequent(self, arr, x, y):
        #code here
        xc=0
        yc=0
        for i in arr:
            if i==x:
                xc+=1
            if i==y:
                yc+=1
        if xc>yc:
            return x
        elif xc<yc:
            return y
        else:
            if x<y:
                return x
            else:
                return y
                
s=Solution()
print(s.moreFrequent([10,20,30,10,7,2,2,2,10,10,7],10,7))
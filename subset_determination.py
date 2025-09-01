#To determine whether b[] is a subset of a[] means a[] should have all the elements 
#present in b[] means repeated elements should be present repeated number of times.
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        
        a.sort()
        b.sort()
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1; j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                return False
        return j == len(b)
    
s=Solution()


#here 20 is present 2 times in b[] so output will be false
print(s.isSubset([10,20,50,60,90,25,90,27,63,101],[10,20,20]))  

print(s.isSubset([10,20,50,60,90,25,90,27,63,20,101],[10,20,50,20]))  

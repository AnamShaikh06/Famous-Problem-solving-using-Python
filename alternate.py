class Solution:
    def alternateSort(self,arr):
        #[1,3,2,4]
        new=[]
        small=sorted(arr)    #[1,2,3,4]
        large=sorted(arr,reverse=True)  #[4,3,2,1]
        n = len(arr)  #4
#new=[4,1,3,2]
        for i in range((n + 1) // 2):  #0,1      
            new.append(large[i])    #4 ,3
            if len(new) < n:        #1<4  ,3<4      
                new.append(small[i])   #1 ,2   
        return new # [4,1,3,2]

s=Solution()
print(s.alternateSort([1,2,4,3]))
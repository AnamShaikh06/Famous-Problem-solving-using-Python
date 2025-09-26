# Input: arr[] = [2, 3, 2, 3, 5]
# Output: [0, 2, 2, 0, 1]
class Solution:
    def frequencyCount(self, arr):
        n=len(arr)
        new=[]   
        freq={} #{2:2,3:2,5:1}
        result=[]
        for i in range(1,n+1):
            new.append(i)  #[1,2,3,4,5]
        for i in arr:
            if i in freq:
                freq[i]+=1
            else: 
                freq[i]=1
       
        for i in new:
            if i in freq:
                result.append(freq[i])
            else:
                result.append(0)
        return result

s=Solution()
print(s.frequencyCount([1,3,4,4,7]))
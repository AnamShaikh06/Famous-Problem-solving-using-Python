#For the given array we have to find the minimum and maximum element in the array.

class Solution:
    def get_min_max(self, arr):
        mini = arr[0]
        maxi = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < mini:
                mini = arr[i]
            elif arr[i] > maxi:
                maxi = arr[i]
        return mini, maxi
                        
s=Solution()
print(s.get_min_max([10,20,50,60,90,-9,-2,109,25,90,27,63,101]))  

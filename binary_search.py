#Search on what index element is found and If multiple occurrences are there, please return the smallest index.
class Solution:
    def binarysearch(self, arr, k):
        st=0
        end=len(arr)-1
        ans=-1
        while(st<=end):
            mid=(st+end)//2
            if arr[mid]==k:
                ans=mid
                end=mid-1
#to return the smallest index if multiple occurrence are present we had used end=mid-1 
            elif arr[mid]<k:
                st=mid+1
            else:
                end=mid-1
        return ans
s=Solution()
print(s.binarysearch([1,8,6,7,6,9],6))
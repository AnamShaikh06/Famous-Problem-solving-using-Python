#Given a sorted array arr consisting of 0s and 1s. The task is to find the index (0-based indexing) of the first 1 in the given array.
#if not available then print -1
#User function Template for python3

class Solution:
    def firstIndex(self, arr):
        st=0
        end=len(arr)-1
        ans=-1
        while st<=end :
            mid=(st+end)//2
            if arr[mid]==1:
                ans=mid
                end=mid-1
            elif arr[mid]<1:
                st=mid+1
            else:
                end=mid-1
        return ans
                
s=Solution()
print(s.firstIndex([0,0,0,1,1,1,1,1]))
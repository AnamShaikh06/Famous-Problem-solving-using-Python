# Given an array arr, rotate the array by one position in clockwise direction.

class Solution:
    def rotate(self, a):
        if len(a) > 1:
            last = a[-1]
            # shift elements to the right
            for i in range(len(a)-1, 0, -1):
                a[i] = a[i-1]
            a[0] = last
        return a
s=Solution()
print(s.rotate([1,2,3,4,5]))
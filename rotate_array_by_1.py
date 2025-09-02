#Rotating the given array by one

class Solution:
    def rotate(self, a):
        if len(a) > 1:
            last = a[-1]
            # shift elements to the right
            for i in range(len(a)-1, 0, -1):
                a[i] = a[i-1]
            a[0] = last

s=Solution()
a=[1,2,3,4,5,6,7]
s.rotate(a)
print(a)
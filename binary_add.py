#addition of two binary numbers

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #int() converts into integer but 2 represents that to convert binary no. to int
        #bin() again converts that number into binary and it is in '0b' prefix 
        #so to remove that prefix we had used slicing concept [2:]
        return bin(int(a,2)+int(b,2))[2:]
s=Solution()
print(s.addBinary('1010','111'))
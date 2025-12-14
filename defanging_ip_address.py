# A defanged IP address replaces every period "." with "[.]"
class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=address.split(".")
        ans="[.]".join(s)
        return ans
s=Solution()
print(s.defangIPaddr("1.5.22.0"))
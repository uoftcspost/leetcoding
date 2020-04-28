class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "*":
            return True
        if p == "?" and len(s) == 1:
            return True
        if len(s) == 0:
            return p == "" or p == "*"

        si = 0
        pi = 0
        








yeet = Solution()
print(yeet.isMatch("a", "aa"))
print(yeet.isMatch("ab", "*"))




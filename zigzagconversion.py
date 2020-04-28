class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        f = []
        for i in range(numRows):
            f.append("")

        down = True
        rip = 0
        for i in range(len(s)):
            f[rip] += s[i]
            if down:
                rip += 1
            else:
                rip -= 1
            if rip == 0 or rip == numRows - 1:
                down = not down

        yeet = ""
        for i in f:
            yeet += i
        return yeet



yeet = Solution()
print(yeet.convert("PAYPALISHIRING", 3))
print(yeet.convert("ab", 1))

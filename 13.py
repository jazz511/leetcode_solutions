class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(len(s)):
            l=s[i]
            if i+1 < len(s):
                if l == 'I' and s[i+1] in ("V","X"):
                    num -= 1
                elif l == 'X' and s[i+1] in ("L","C"):
                    num -= 10
                elif l == 'C' and s[i+1] in ("D","M"):
                    num -= 100
                else:
                    num += d[l]
            else:
                num += d[l]
        return num

A=Solution()
print(A.romanToInt("MCMXCIV"))

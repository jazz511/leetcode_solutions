class Solution:
    def reverse(self, x: int) -> int:
        num = int('-'+str(abs(x))[::-1] if str(x)[0]=='-' else str(abs(x))[::-1])
        return num if -231 <= num < 231 else 0

print(Solution().reverse(1646324359))
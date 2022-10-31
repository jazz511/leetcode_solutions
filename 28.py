class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=len(haystack)
        if l == 0: return 0
        i=0
        j=len(needle)
        if l<j: # early termination
            return -1
        a=needle[0]
        while i<l-j+1:
            print(i,haystack[i:i+j])
            if haystack[i] == a and haystack[i:i+j] == needle:
                    return i
            else: i+=1
        return -1

print(Solution().strStr("mississippi","issip"))
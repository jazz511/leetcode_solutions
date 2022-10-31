class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=len(s)
        for i in range(l//2 + l%2):
            if s[i] == s[l-1-i]:
                pass
            elif s[i] == s[l-2-i]:
                #element from right can be skiped
                #check if remaining string is palindrome
                str = s[i+1:l-2-i]
                if str != str[::-1]:
                    #Edge case: ebcbbececabbacecbbcbe
                    if s[i+1] == s[l-1-i]:
                        #current element can be skiped
                        #check if remaining string is palindrome
                        str = s[i+2:l-1-i]
                        return str == str[::-1]
                    else: return False
                else: return True
            elif s[i+1] == s[l-1-i]:
                #current element can be skiped
                #check if remaining string is palindrome
                str = s[i+2:l-1-i]
                return str == str[::-1]
            else:
                return False
        else: return True

## Simplified code from leetcode discussion
    def validPalindrome2(self, s: str) -> bool:
            p1=0
            p2=len(s)-1
            while p1<=p2:
                if s[p1]!=s[p2]:
                    string1=s[:p1]+s[p1+1:]
                    string2=s[:p2]+s[p2+1:]
                    return string1==string1[::-1] or string2==string2[::-1]
                p1+=1
                p2-=1
            return True

print(Solution().validPalindrome("ebcbbececabbacecbbcbe"))

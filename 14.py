from unittest.util import sorted_list_difference


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i=0
        l = min(strs, key=len)
        a=""
        for i,c in enumerate(l):
            if all(x[i]==c for x in strs ):
                a +=c
            else:
                return l[:i]
        return a
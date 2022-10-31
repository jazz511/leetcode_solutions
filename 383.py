class Solution:
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        #l = [x for x in magazine]
        for x in ransomNote:
            #if x in l:l.remove(x)
            if x in magazine: magazine = magazine.replace(x,"",1)
            else: return False
        return True


##Oneliner
# set -> only unique items

#    but above sol is only O(N) whereas for below soln
#    O(N) to construct set(ransomNote
#    O(N) for ransomNote.count(c), but this is done N times, so O(N^2)
#    O(M) for magazine.count(c), but this is done N times, so O(N * M)
#    So in the end it's O(N^2) + O(N * M).

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(i) <= magazine.count(i) for i in set(ransomNote))

A = Solution()
print(A.canConstruct("aabb", "aab"))

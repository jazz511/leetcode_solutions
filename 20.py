class Solution:
    def isValid(self, s: str) -> bool:
        length=len(s)

        #No need of this after IndexError exception being handled
        if length == 1:
            return False

        keys={'(':')', '{': '}', '[':']'}
        i=0
        l=list(s)
        while i < length:
            print(i, l, length)
            e=l[i]
            try:
                if keys[e] == l[i+1]:
                    l.pop(i+1),l.pop(i)
                    if i >0: i-=1
                else:
                    i+=1
            except (KeyError,IndexError):
                #return False if its a closing bracket
                #or the string ends with a opening bracket
                return False
            length=len(l)
        return not i

s = "(()){}{}[[[]]]["
print(Solution().isValid(s))
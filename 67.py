class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=''
        carry=0
        length=max(len(a),len(b))
        a,b=a.zfill(length), b.zfill(length)
        for i in range(length-1,-1,-1):
            # if a[i] == '0':
            #     if b[i] == '0':
            #         if carry:
            #             res+= '1'
            #             carry=0
            #         else: res+='0'
            #     else:
            #         if carry: res+= '0'
            #         else: res+='1'
            # else:
            #     if b[i] == '0':
            #         if carry: res+= '0'
            #         else: res+='1'
            #     else:
            #         if carry: res+='1'
            #         else:
            #             res+='0'
            #             carry=1
            sum = int(a[i]) + int(b[i]) + carry
            res += str(sum%2)
            carry = sum//2
        if carry: res+='1'
        return res[::-1]

a='11'
b='1'
print(Solution().addBinary(a,b))


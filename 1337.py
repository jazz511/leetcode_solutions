class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        s=sorted(mat)
        a=[]
        for i in range(k):
            x=mat.index(s[i])
            a.append(x)
            mat[x]=-1
        return a

 #OLD
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        c=[]
        for m in mat:
            c.append(m.count(1))
        s=sorted(c)
        a=[]
        for i in range(k):
            x=c.index(s[i])
            a.append(x)
            c[x]=-1
        return a

mat =[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3

print(Solution().kWeakestRows(mat,k))

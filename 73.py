class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        a=b=False
        for i in range(m):

            for j in range(n):
                if matrix[i][j] == 0:
                    # check if its the 1st row or col so later we
                    # can set all the 1st row or col elements as 0
                    if i == 0:a=True
                    if j == 0:b=True

                    matrix[i][0]=matrix[0][j]=0

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = 0 if matrix[0][j] == 0 or matrix[i][0] == 0 else matrix[i][j]

        # update the first row and col if they're zero
        if a:
            for j in range(n):
                matrix[0][j] = 0
        if b:
            for i in range(m):
                matrix[i][0] = 0
        
        return matrix

m1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

m2 = [[1,2,3,4],
      [5,0,7,8],
      [0,10,11,12],
      [13,14,15,0]]

#print(Solution().setZeroes(m1))
print(Solution().setZeroes(m2))
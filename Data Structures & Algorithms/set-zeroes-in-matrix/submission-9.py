class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        fr,fc = False,False
        for i in range(1,m):
            if matrix[i][0] == 0: 
                fc = True
                break
        for j in range(1,n):
            if matrix[0][j] == 0:
                fr = True
                break
        if matrix[0][0] == 0: fr,fc = True, True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if fr:
            for i in range(1,n): matrix[0][i] = 0
        if fc:
            for i in range(1,m): matrix[i][0] = 0
        if fr or fc : matrix[0][0] = 0
        
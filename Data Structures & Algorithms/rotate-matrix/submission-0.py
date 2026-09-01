class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        n = len(mat)
        for i in range(0,n//2): mat[i],mat[n-i-1] = mat[n-1-i],mat[i]
        for i in range(0,n):
            for j in range(i+1,n): mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
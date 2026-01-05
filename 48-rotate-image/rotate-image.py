class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        res=[[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                res[j][n-1-i]=matrix[i][j]
        matrix[:]=res

        
        
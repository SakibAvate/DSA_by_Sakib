class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_track = [0 for _ in range(rows)]
        col_track = [0 for _ in range(cols)]

        for i in range(0,rows):
            for j in range(0, cols):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1
        
        for i in range(0,rows):
            for j in range(0, cols):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0         

        
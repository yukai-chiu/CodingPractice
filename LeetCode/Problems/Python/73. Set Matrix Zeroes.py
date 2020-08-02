#Time: O(mn)
#Space: O(1)
class Solution:
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        is_col = False
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0 and matrix[i][j] == 0:
                    is_col = True
                elif matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
                    
        if is_col: 
            for i in range(len(matrix)):
                matrix[i][0] = 0

#Time: O(mn)
#Space: O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
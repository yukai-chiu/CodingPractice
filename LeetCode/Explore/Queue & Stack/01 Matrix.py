class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return matrix
        
        
        nearest = [[float('inf')] * len(matrix[0]) for _ in range(len(matrix))]
        queue = []
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    nearest[i][j] = 0
                    queue.append((i,j))
        
        #traverse all the zeros, and update the nearest val in the matrix
        while queue:
            r, c = queue.pop(0)
            for d in directions:
                new_r = r + d[0]
                new_c = c + d[1]
                if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]):
                    if nearest[new_r][new_c] > nearest[r][c] + 1:
                        nearest[new_r][new_c] = nearest[r][c] + 1
                        queue.append((new_r, new_c))
        
        return nearest
        
        
            
        
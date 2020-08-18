#Time: O(mn)
#Space: O(mn)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        
        M = len(grid)
        N = len(grid[0])
        
        def checkIsland(i, j):
            if i < 0 or i >= M or j < 0 or j >=N:
                return 0
            if grid[i][j] == 1:
                return 1
    
            grid[i][j] = 1
            left = checkIsland(i, j-1)
            right = checkIsland(i, j+1)
            top = checkIsland(i-1, j)
            bottom = checkIsland(i+1, j)
            
            return left and right and top and bottom
            
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    islands+= checkIsland(i,j)
        return islands

#Time: O(mn)
#Space: O(mn)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        
        M = len(grid)
        N = len(grid[0])
        visited = set()

        def checkIsland(i, j):
            if i < 0 or i >= M or j < 0 or j >=N:
                return 0
            if (i,j) in visited or grid[i][j] == 1:
                return 1
            visited.add((i,j))
            left = checkIsland(i, j-1)
            right = checkIsland(i, j+1)
            top = checkIsland(i-1, j)
            bottom = checkIsland(i+1, j)
            
            return left and right and top and bottom
            
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0 and (i,j) not in visited:
                    islands+= checkIsland(i,j)
        return islands
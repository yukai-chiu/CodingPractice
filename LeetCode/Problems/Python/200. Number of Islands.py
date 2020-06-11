#BFS
#Time: O(m*n)
#Space: O(m*n)
class Solution:
    
    def bfs(self, curr, visited, grid):
        
        queue = [curr]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while queue:
            curr = queue.pop(0)
            
            for d in directions:
                if 0 <= curr[0] + d[0] < len(grid) and 0 <= curr[1]+d[1] < len(grid[0]):
                    next_pos = (curr[0] + d[0],curr[1] + d[1])
                    if grid[next_pos[0]][next_pos[1]] == "1" and next_pos not in visited:
                        visited[next_pos] = True
                        queue.append(next_pos)

        return visited
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        visited = {}
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans +=1
                    
                    visited = self.bfs((i,j), visited, grid)

        return ans

#DFS
#Time: O(m*n)
#Space: O(m*n)
class Solution:
    def dfs(self, grid, row, col, visited):
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        stack = [(row,col)]
        while stack:
            r, c = stack.pop()
            for d in direction:
                new_r = r+d[0]
                new_c = c+d[1]
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                    if grid[new_r][new_c] == '1' and (new_r,new_c) not in visited:
                        visited[(new_r,new_c)] = True
                        stack.append((new_r,new_c))
                        
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
   
        visited = {}
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row,col) not in visited:
                    num_islands+=1
                    visited[(row,col)] = True
                    self.dfs(grid, row, col, visited)
                    
                        
        return num_islands
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
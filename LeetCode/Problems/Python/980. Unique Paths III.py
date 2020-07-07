#Time: O(4^(m*n))
#Space: O(m*n)
class Solution:
    def walk(self, i, j, grid, visited, remain_steps):
        if remain_steps == 0:
            if grid[i][j] == 2:
                return 1
            else:
                return 0
        
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        path_count = 0
        for d in direction:
            new_i = i + d[0]
            new_j = j + d[1]

            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                if grid[new_i][new_j] != -1 and not visited[new_i][new_j]:
           
                    visited[new_i][new_j] = True
                    path_count += self.walk(new_i, new_j, grid, visited, remain_steps-1)
                    visited[new_i][new_j] = False

        return path_count

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        total_steps = 0
        start = [0,0]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    total_steps+=1
                if grid[i][j] == 1:
                    start = [i,j]
        
        visited[start[0]][start[1]] = True
        total_steps+=1
     
        return self.walk(start[0], start[1], grid, visited, total_steps) 
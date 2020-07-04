#BFS
#Time: O(m*n)
#Space: O(m*n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
       
        mins = -1
        M = len(grid)
        N = len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
     
            
        queue = []
        fresh = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        if not queue and not fresh:
            return 0
        
        if not queue:
            return -1
        
        while queue:
            mins+=1
            for _ in range(len(queue)):
                cur = queue.pop(0)
                for d in directions:
                    new_i = cur[0] + d[0]
                    new_j = cur[1] + d[1]
                    if 0 <= new_i < M and 0 <= new_j < N:
                        if grid[new_i][new_j] == 1:
                            queue.append((new_i,new_j))
                            grid[new_i][new_j] = 2
                            fresh-=1
  
        if fresh:
            return -1
        return mins
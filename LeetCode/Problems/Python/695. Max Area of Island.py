class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_area = 0
        
        M = len(grid)
        N = len(grid[0])
        visited = set()
        
        def calculateArea(i, j):
            direction = [[1,0],[0,1],[-1,0],[0,-1]]
            queue = deque()
            queue.append((i,j))
            curr_area = 1
            while queue:
                i,j = queue.popleft()
                for d in direction:
                    new_i = i+d[0]
                    new_j = j+d[1]
                    if 0<=new_i<M and 0<=new_j<N and grid[new_i][new_j] == 1 and (new_i,new_j) not in visited:
                        visited.add((new_i, new_j))
                        queue.append((new_i,new_j))
                        curr_area+=1
            return curr_area
            
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    max_area = max(max_area, calculateArea(i,j))
        
        return max_area
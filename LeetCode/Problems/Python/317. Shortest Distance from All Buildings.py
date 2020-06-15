class Solution:
    def bfs(self, grid, i, j):
        visited = [[False] * self.n for _ in range(self.m)]
        visited[i][j] = True
        building_count = 1
        queue = [(i, j, 0)]
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        while queue:
            x, y, distance = queue.pop(0)
            for d in direction:
                new_x = x+d[0]
                new_y = y+d[1]
                if 0<=new_x<self.m and 0<=new_y<self.n and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    if grid[new_x][new_y] == 0:
                        queue.append((new_x,new_y, distance+1))
                        self.hit[new_x][new_y]+=1
                        self.dist[new_x][new_y]+= distance+1
                    elif grid[new_x][new_y] == 1:
                        building_count+=1
        return building_count == self.buildings
        
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        self.m = len(grid)
        self.n = len(grid[0])
        self.hit = [[0] * self.n for _ in range(self.m)]
        self.dist = [[0] * self.n for _ in range(self.m)]
        self.buildings = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.buildings+=1
        
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    if not self.bfs(grid, i, j):
                        return -1
                    
        result = float('inf')
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0 and self.hit[i][j] == self.buildings:
                    result = min(self.dist[i][j], result)
        print(self.dist, self.hit)            
        return result if result != float('inf') else -1
                    
#counting
#Time: O(m*n) 
#Space: O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:       
        
        if not grid:
            return 0
        
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    
                    #check left
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter-=2
                    
                    #check up
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter-=2
                        
                    
        return perimeter


#Time: O(m*n) worst case
#Space: O(min(m,n))
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #bfs with queue
        #see how many neighbors
        #1: 3 edges, 2: 2 edges, 3: 1 edges
        
        
        if not grid:
            return 0
        
        perimeter = 0
        
        
        queue = deque()
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    #bfs(i,j)
                    queue.append((i,j))
                    visited.add((i,j))
                    while queue:
                        curr = queue.popleft()
                        neighbor = 0
                        for d in direction:
                            new_i = curr[0] + d[0]
                            new_j = curr[1] + d[1]
                            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                                if grid[new_i][new_j] == 1:
                                    if (new_i, new_j) not in visited:
                                        visited.add((new_i, new_j))
                                        queue.append((new_i, new_j))
                                    neighbor+=1
    
                        perimeter += (4-neighbor)
                    return perimeter
        
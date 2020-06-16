#Time: O(m*n)
#Space: O(m*n)
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        
        def bfs(i, j):
            direction = [(1,0), (0,1), (-1,0), (0,-1)]
            visited[i][j] = True
            queue = [(i,j)]
            island = [(0,0)]
            while queue:
                r, c = queue.pop(0)
                for d in direction:
                    new_i = r + d[0]
                    new_j = c + d[1]
                    if 0 <= new_i < M and 0 <= new_j < N and grid[new_i][new_j] == 1:
                        if visited[new_i][new_j] == False:
                            visited[new_i][new_j] = True
                            queue.append((new_i, new_j))
                            island.append((new_i-i, new_j-j))
            return tuple(island)
        
        M = len(grid)
        N = len(grid[0])
        visited = [[False] * N for _ in range(M)]
        islands = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and not visited[i][j]:
                    #start bfs
                    islands.add(bfs(i, j))
        
        
        return len(islands)
#Time: O(m*n)
#Space: O(m*n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        M = len(grid)
        N = len(grid[0])
        dp = [[0] * N for _ in range(M)]
        
        dp[0][0] = grid[0][0]
        for i in range(1, M):
            dp[i][0] = grid[i][0] + dp[i-1][0]
            
        for j in range(1, N):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        
        for i in range(1, M):
            for j in range(1, N):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
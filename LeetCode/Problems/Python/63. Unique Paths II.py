#Time: O(m*n)
#Space: O(m*n)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
             return 0
        if obstacleGrid[0][0] == 1:
            return 0
        
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        dp = [[0] * N for _ in range(M)]
        
        for i in range(M):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
            
        for j in range(N):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        
        for i in range(1, M):
            for j in range(1, N):
                #if it's not obstacle
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        
        return dp[-1][-1]
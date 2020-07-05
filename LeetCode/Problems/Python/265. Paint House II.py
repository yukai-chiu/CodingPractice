#Dynamic programming
#Time: O(n*k^2)
#Space: O(n)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        k = len(costs[0])
        dp = [[0] * k for _ in range(len(costs))]
        dp[0] = costs[0]
        
        for i in range(1, len(costs)):
            for j in range(k):
                dp[i][j] = min(dp[i-1][:j]+ dp[i-1][j+1:]) + costs[i][j]
    
        return min(dp[-1])
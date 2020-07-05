#Dynamic programming
#Time: O(n)
#Space: O(1)
class Solution:   
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        current = [0]*3
        previous = [0]*3
        
        for i in range(len(costs)):
            current[0] = min(previous[1], previous[2]) + costs[i][0]
            current[1] = min(previous[0], previous[2]) + costs[i][1]
            current[2] = min(previous[0], previous[1]) + costs[i][2]
            previous = current.copy()
    
        return min(current)

#Dynamic programming
#Time: O(n)
#Space: O(n)
class Solution:   
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        dp = [[0] * 3 for _ in range(len(costs))]
        dp[0] = costs[0]
        
        for i in range(1, len(costs)):
            for j in range(3):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j-2]) + costs[i][j]
    
        return min(dp[-1])

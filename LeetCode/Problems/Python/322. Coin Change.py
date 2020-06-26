#Dynamica programming
#Time: O(S*n)
#Space: O(n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount == 0:
            return 0
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i-c >=0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
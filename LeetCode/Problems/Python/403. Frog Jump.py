#Dynamic programming
#Time: O(n^2)
#Space: O(n^2)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return False
        S = len(stones)
        
        dp = dict((x,set()) for x in stones)
        
        if 1 in dp:
            dp[1].add(1)
        else:
            return False
        
        for i in range(1, S):
            for k in dp[stones[i]]: 
                for step in [k-1,k,k+1]:
                    if step > 0 and stones[i]+step in dp:
                        dp[stones[i]+step].add(step)

        return dp[stones[-1]] != set()
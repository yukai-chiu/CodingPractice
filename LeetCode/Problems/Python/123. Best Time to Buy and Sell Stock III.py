#Bidirectional DP
#Time: O(n)
#Space: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        
        length = len(prices)
        
        left_dp = [0] * length
        #we add one because we also want to consider the case when only 1 transaction
        right_dp = [0] * (length+1)
        
        
        left_min = prices[0]
        right_max = prices[-1]
        for i in range(1,length):
            left_dp[i] = max(left_dp[i-1], prices[i] - left_min)
            left_min = min(left_min, prices[i])
            
            right_dp[-i-1] = max(right_dp[-i], right_max - prices[-i-1])
            right_max = max(right_max, prices[-i-1])
            
        #print(right_dp)
        #print(left_dp)
        
        
        
        #max profit of two transaction
        max_profit = 0
        for i in range(length):
            max_profit = max(max_profit, left_dp[i]+right_dp[i+1])
            
        return max_profit


#Simulation
#Time: O(n)
#Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        
        length = len(prices)
        
        max_profit = 0
        t1_cost = float('inf')
        t2_cost = float('inf')
        t1_profit = 0
        t2_profit = 0
        for i in range(length):
            t1_cost = min(t1_cost, prices[i])
            t1_profit = max(t1_profit, prices[i]-t1_cost)
            t2_cost = min(t2_cost, prices[i]-t1_profit)
            t2_profit = max(t2_profit, prices[i]-t2_cost)
            
        return t2_profit
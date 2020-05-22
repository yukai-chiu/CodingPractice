#One pass
#Time: O(n)
#Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0  
        maxProfit = 0
        
        for i in range(len(prices) -1, 0, -1):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
       
        return maxProfit
 

#Time: O(n)
#Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        maxProfit = 0
        valley = prices[0]
        peak = prices[0]
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i+=1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i+=1
            peak = prices[i]

            maxProfit += peak - valley
            
        return maxProfit
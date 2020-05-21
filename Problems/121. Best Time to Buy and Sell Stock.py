#brute-force
#Time: O(n^2)
#Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        result = 0
        
        for i in range(len(prices)):
            for j in range(len(prices) - i):
                result = max(prices[i + j] - prices[i], result)
                
        return result

#One pass
#Time: O(n)
#Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minPrice = float('inf')
        maxProfit = 0
        #brute-force
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
                
        return maxProfit
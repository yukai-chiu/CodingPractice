#my dp
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        
        #positive & negative
        dp = [[0] * len(nums) for _ in range(2)]
        max_prod = float('-inf')
        
        for i in range(len(nums)):
            if i == 0:
                dp[0][i] = nums[i]
                dp[1][i] = nums[i]
            else:
                
                dp[1][i] = min(dp[1][i-1] * nums[i], dp[0][i-1] * nums[i], nums[i])
                dp[0][i] = max(dp[1][i-1] * nums[i], dp[0][i-1] * nums[i], nums[i])
                        
   
            max_prod = max(max_prod, dp[0][i])
  
        
        return max_prod


#clear, less space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        
        max_prod = nums[0]
        cur_max =max_prod
        cur_min =max_prod
        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(cur_max * nums[i], nums[i])
            cur_min = min(cur_min * nums[i], nums[i])
   
            max_prod = max(max_prod, cur_max)
  
        
        return max_prod
#Dynamica Programming
#Time: O(n)
#Space: O(n)
class Solution: 
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0   
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            #the maximum of "if we rob this": this value + max profit from i-2, since we won't be robbing i-1 in this case
            # and "if we don't rob this": the maximum value from i - 1
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])  
        return dp[-1]


#Dynamica Programming, optimizing space
#Time: O(n)
#Space: O(1)
class Solution: 
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0   
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        pick = nums[0]
        no_pick = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            #the maximum of "if we rob this": this value + max profit from i-2, since we won't be robbing i-1 in this case
            # and "if we don't rob this": the maximum value from i - 1
            curr = max(pick + nums[i], no_pick)  
            pick, no_pick = no_pick, curr
        return no_pick
        
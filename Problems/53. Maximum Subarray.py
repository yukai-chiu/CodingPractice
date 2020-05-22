#Time: O(n)
#Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum = float('-inf')
        curr_sum = float('-inf')
        for n in nums:
            curr_sum = max(n, curr_sum + n)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

#Time: O(n)
#Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum = float('-inf')
        for i in range(1, len(nums)):
            #restart if local maximum < 0, just drop them
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])
        return max_sum
                
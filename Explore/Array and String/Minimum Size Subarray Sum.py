class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        l = 0
        sub_sum = 0
        ans = float('inf')

        for i in range(len(nums)):
            sub_sum += nums[i]
            while sub_sum >= s:
                ans = min(ans, i - l +1)
                sub_sum -= nums[l]
                l += 1
                
        return ans if ans != float('inf') else 0
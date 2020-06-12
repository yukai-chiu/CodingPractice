#Math
#Time: O(n)
#Space: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ref_sum = (1+ len(nums)) * len(nums)//2
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
        return ref_sum - curr_sum
#Time: O(n)
#Space: O(1)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or not k:
            return 0
        if k <=1:
            return 0
        
        l = 0
        result = 0
        product = 1
        
        for r, val in enumerate(nums):
            product*= val
            while product >= k:
                product /= nums[l]
                l+=1
            result+=(r-l+1)

        return result 
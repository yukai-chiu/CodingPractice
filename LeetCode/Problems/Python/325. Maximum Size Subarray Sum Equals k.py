#hashmap
#Time: O(n)
#Space: O(n)
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        lookup = {0:-1}
        prefix_sum = 0
        max_size = 0
        for i, n in enumerate(nums):
            prefix_sum+=n
            if prefix_sum - k in lookup:
                max_size = max(max_size, i-lookup[prefix_sum-k])
                
            if prefix_sum not in lookup:
                lookup[prefix_sum] = i
    
        return max_size
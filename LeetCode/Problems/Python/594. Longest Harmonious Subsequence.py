class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = Counter(nums)
        
        max_length = 0
        for c in count:
            if count[c-1] != 0:
                max_length = max(max_length, count[c] + count[c-1])
                
        return max_length
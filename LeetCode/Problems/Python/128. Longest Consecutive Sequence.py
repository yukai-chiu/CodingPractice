class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique = set(nums)
        max_length = 0
        for n in unique:
            if n-1 not in unique:
                curr_length = 1
                curr = n
                while curr+1 in unique:
                    curr+=1
                    curr_length+=1
         
                max_length = max(max_length, curr_length)
        return max_length
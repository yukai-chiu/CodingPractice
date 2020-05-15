class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        j = 0
        for n in nums[1:]:
            if nums[j] != n:
                nums[j+1] = n
                j+=1
        return j + 1
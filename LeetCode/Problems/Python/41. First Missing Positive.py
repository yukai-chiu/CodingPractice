#Time: O(n)
#Space: O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        
        exist = set()
        
        for n in nums:
            exist.add(n)
        
        for i in range(1,len(nums)+1):
            if i not in exist:
                return i
        
        return len(nums)+1
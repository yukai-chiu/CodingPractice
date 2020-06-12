#my first try
#Time: O(n*n!)
#Space: O(n!)
class Solution:
    def backtrack(self, nums, result, curr):
        if len(nums) == 0:
            result.add(tuple(curr))
            
        for i in range(len(nums)):
            self.backtrack(nums[:i]+nums[i+1:], result, curr + [nums[i]])
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [] 
        
        result = set()
        self.backtrack(nums, result, [])
        return result

#use sorting first to handle duplicate
#Time: O(n*n!)
#Space: O(n!)
class Solution:
    def backtrack(self, nums, result, curr):
        if len(nums) == 0:
            result.append(curr)
            
        for i in range(len(nums)):
            if i == 0 or nums[i]!= nums[i-1]:
                self.backtrack(nums[:i]+nums[i+1:], result, curr + [nums[i]])
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [] 
        
        result = []
        nums.sort()
        self.backtrack(nums, result, [])
        return result
    
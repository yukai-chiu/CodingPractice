#value as index, and swap to correct position
#Time: O(n)
#Space: O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        
        for i in range(len(nums)):
            #swap it with the correct index position
            while nums[i] > 0 and nums[i] <=len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        
        return len(nums)+1

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
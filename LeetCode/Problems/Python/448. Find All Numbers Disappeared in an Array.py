#Time: O(n)
#Space: O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        
        result = []
        for n in nums:
            if nums[abs(n)-1] > 0:
                nums[abs(n)-1] *= -1

        for i,n in enumerate(nums):
            if n>0: 
                result.append(i+1)
        
        return result

#hash map
#Time: O(n)
#Space: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        result = set([x for x in range(1, len(nums)+1)])
        
        for n in nums:
            if n in result:
                result.discard(n)
        
        return result
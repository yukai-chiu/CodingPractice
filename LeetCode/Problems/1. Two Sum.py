#Old Implementation
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return -1
        complement = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp not in complement:# and i != complement[target - n]:
                complement[n] = i
            else:
                return [complement[comp], i]



#One-pass hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #build a dict storing index and complements
        #iterate through the list and check if we've seen the complement
        if not nums:
            return []
        comp = {}
        
        for i,n in enumerate(nums):
            if n in comp:
                return [comp[n],i]
            else:
                comp[target-n] = i
                

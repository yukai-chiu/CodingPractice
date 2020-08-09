#Time: O(n*2^n)
#Space: O(n*2^n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        subsets = [[]]    
        start = 0
        for i, n in enumerate(nums):
            if i == 0 or nums[i] != nums[i-1]:
                start = 0
            elif nums[i] == nums[i-1]:
                start = end
            end = len(subsets)
            for i in range(start, end):
                subsets.append(subsets[i]+[n]) 
        return subsets


#Time: O(n*2^n)
#Space: O(n*2^n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        subsets = [[]]
        seen = set(())
        for n in nums:
            prev = len(subsets)
            for i in range(prev):
                temp = subsets[i].copy()
                if tuple(temp+[n]) in seen:
                    continue
                else:
                    seen.add(tuple(temp+[n]))
                    subsets.append(temp+[n])
        return subsets

#Handle duplicate
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        subsets = [[]]      
        for i, n in enumerate(nums):
            if i == 0 or nums[i] != nums[i-1]:
                temp = []
                for i in subsets:
                    temp.append(i+[n])
                subsets.extend(temp)
            elif nums[i] == nums[i-1]:
                temp2 = []
                for i in temp:
                    temp2.append(i+[n])
                subsets.extend(temp2)
                temp = temp2
        return subsets

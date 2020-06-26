#DFS
#Time: O(n*n!), n for slicing nums, and n! recursion
#Space: O(n!)
class Solution:
    def dfs(self, nums, result, curr):
        if len(nums) == 0:
            result.append(curr)
           

        for i, n in enumerate(nums):
            #the rest of the nums except the current i
            self.dfs(nums[:i] + nums[i+1:], result, curr + [nums[i]])

    
    def permute(self, nums: List[int]) -> List[List[int]]:
        result =[]
        
        self.dfs(nums, result, [] )
        return result


class Solution:
    def permutation(self, nums, result, curr, idx):
        if idx == len(nums):
            result.append(nums[:])
            return
            
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.permutation(nums, result, curr, idx+1)
            nums[idx], nums[i] = nums[i], nums[idx]
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        self.permutation(nums, result, [], 0)
        
        return result
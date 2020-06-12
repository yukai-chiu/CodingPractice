#DFS
#Time: O(n*n!), n for slicing nums, and n! recursion
#Space: O(n!)
class Solution:
    def dfs(self, nums, result, curr, target):
        if len(nums) == 0:
            result.append(curr)
           

        for i, n in enumerate(nums):
            #the rest of the nums except the current i
            self.dfs(nums[:i] + nums[i+1:], result, curr + [nums[i]], target)

    
    def permute(self, nums: List[int]) -> List[List[int]]:
        result =[]
        
        self.dfs(nums, result, [], len(nums) )
        return result
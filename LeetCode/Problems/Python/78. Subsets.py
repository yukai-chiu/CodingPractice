#bit manipulation
#Time: O(n * 2^n)
#Space: (n * 2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            #print(bin(i))
            bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
            
        return output
#cascading
#Time: O(n * 2^n)
#Space: (n * 2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        for i in range(n):
            size = len(output)
            for j in range(size):
                cur = output[j].copy()
                cur.append(nums[i])
                output.append(cur)
        return output

        
#backtracking
#Time: O(n * 2^n)
#Space: (n * 2^n)class Solution:
    def backtracking(self, nums, idx, curr, target, output):
        if len(curr) == target:
            output.append(curr)
            
        for i in range(idx, len(nums)):
            self.backtracking(nums, i+1, curr+[nums[i]], target, output)
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        n = len(nums)
        output = []
        for i in range(n+1):
            self.backtracking(nums, 0, [], i, output)
        return output
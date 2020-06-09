#General solution of ksum
#Time: O(n^(k-2))
#Space: O(n) --> O(k) for recursion but worse case is O(n)
class Solution:
    def kSum(self, nums, k, target):
        res = []
        #input check
        if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
            return res
        
        if k == 2:
            return self.twoSum(nums,target)
        
        #use recursion to form the for loop
        for i, n in enumerate(nums):
            if i==0 or n != nums[i-1]:
                for s in self.kSum(nums[i+1:], k-1, target-nums[i]):
                    res.append([nums[i]]+s)
        
        return res
        
        
    def twoSum(self, nums, target):
        l = 0
        r = len(nums)-1
        res = []
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                res.append([nums[l],nums[r]])
                l+=1
                r-=1
            elif sum < target:
                l+=1
            else:
                r-=1
            #skip duplicated
            while l < r and l>0 and nums[l] == nums[l-1]:
                l+=1
            while l < r and r<len(nums)-1 and nums[r] == nums[r+1]:
                r-=1
        return res
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        #basically it's 3sum adding 1 more loop
        #we can also generalize it to ksum
        #it will be k-2 loops + two pointers to find two sum
        nums.sort()
        
        ans = self.kSum(nums, 4, target)
    

        return ans
                        
                    
                    
                
                
                
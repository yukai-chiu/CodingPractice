#My first try
#Time: O(nk)
#Space: O(1)
class Solution:
    def nextPermute(self, nums):
        l = len(nums) -1
        r = len(nums) -1
        target = len(nums) -1
        
        #pick the left index to exchange
        #we need to find the first l-1 that is smaller than l 
        while l > 0 and nums[l] <= nums[l-1]:
            l-=1
        #if we went all the way to the front
        if l == 0:
            nums.reverse()
        
        #next we need to find a digit on the right of 
        else:
            while nums[target] <= nums[l-1]:
                target-=1
            
            nums[l-1], nums[target] = nums[target], nums[l-1]
        
            #make sure that it's the smallest order
            #we will reverse the right part of l-1
            while l < r:
                nums[r], nums[l] = nums[l], nums[r]
                r-=1
                l+=1
        return nums
    def getPermutation(self, n: int, k: int) -> str:
        
        nums = [str(i) for i in range(1,n+1)]
        for i in range(k-1):
            nums = self.nextPermute(nums)
        return "".join(nums)
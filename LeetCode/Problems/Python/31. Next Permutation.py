#Old implementation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums) -1
        r = len(nums) -1
        target = len(nums) -1
        
        
        while(l > 0 and nums[l-1] >= nums[l]):
            l -=1
        if(l == 0):
            nums.reverse()
        
        
        else:
            while(nums[target] <= nums[l-1]):
                target -=1
            nums[l-1], nums[target] = nums[target], nums[l-1]
            
            while(l<r):
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            
#Time:O(n)
#Space: O(1)            
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
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
            print(target, l)
            nums[l-1], nums[target] = nums[target], nums[l-1]
        
            #make sure that it's the smallest order
            #we will reverse the right part of l-1
            while l < r:
                nums[r], nums[l] = nums[l], nums[r]
                r-=1
                l+=1
            
            
                
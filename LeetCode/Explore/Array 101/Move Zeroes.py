class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #brute force:
        #initial array with same size of 0's, iterate through the array and set each non-zero from front
        if not nums:
            return
        
        temp = nums.copy()
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+=1
        
        for i in range(j,len(nums)):
            nums[i] = 0
        
        
        
        
        #two pointers
        #one find the next zero, and one find the next non-zero to swap
        #after swap, start from the non-zero pos to continue find the next zero
        
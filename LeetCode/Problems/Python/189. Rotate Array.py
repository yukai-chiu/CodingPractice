#Reverse
#Time:O(n)
#Space:O(1)

class Solution:
    def reverse(self, nums, start, end) -> None:
        while start < end:
            nums[start] ,nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)-1
        k = k % len(nums)
        
        self.reverse(nums, 0, n)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n)
        return

#Use extra space
#Time: O(n)
#Space: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        temp = nums.copy()
        for i in range(len(nums)):
            nums[(i+k)%len(nums)] = temp[i]
        return

#Rotate 1 at a time
#Time:O(kn)
#Space:O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        while k:
            last = nums[-1]
            for i in range(len(nums)-1,0,-1):
                nums[i] = nums[i-1]
            nums[0] = last
            
            k-=1
        return
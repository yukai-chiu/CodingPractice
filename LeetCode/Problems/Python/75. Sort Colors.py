#One pass three pointer
#Time: O(n)
#Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0 #keep track of the bound of 0's
        curr = 0 # traverse through the list and see if we want to swap with 0 or 2
        p2 = len(nums)-1 #keep track of the bound of 2's
        
        while curr <=p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0+=1
                curr+=1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2-=1
            else:
                curr+=1

#Two pass with counter
#Time: O(n)
#Space: O(n)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        idx = 0
        for n in range(3):
            for i in range(count[n]):
                nums[idx+i] = n
            idx += count[n]



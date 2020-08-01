#Bubble sort: TLE
#Time: O(n^2)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #bubble sort
        for i in range(len(nums)):
            swapped = False
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    swapped = True
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            if not swapped:
                break
        return nums
#Quick sort
#Time: O(nlogn)
class Solution:
    def quickSort(self, nums, l, r):
        if l < r:
            pivot = self.partition(nums, l, r)
            self.quickSort(nums, l, pivot-1)
            self.quickSort(nums, pivot+1, r)
            
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l
        for j in range(l, r):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
        nums[i], nums[r] = nums[r], nums[i]
        return i
            
    def sortArray(self, nums: List[int]) -> List[int]:
   
        self.quickSort(nums, 0, len(nums)-1)
        
        return nums
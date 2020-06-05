class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        #binary search
        l = 0
        r = len(nums) -1
        #find the idx where nums[i] > nums[i+1]
        #which means find the pivot, the pivot will be the minimum
        pivot = 0
        if nums[l] < nums[r]:
            return nums[0]
        
        while l <= r:
            mid = l + (r-l)//2
            print(mid)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            else:
                #pivot on the right?
                if nums[mid] < nums[l]:
                    r = mid-1 
                else:
                    l = mid+1 
        
#Solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        #binary search
        l = 0
        r = len(nums) -1
        #find the idx where nums[i] > nums[i+1]
        #which means find the pivot, the pivot will be the minimum
        pivot = 0
        if nums[l] < nums[r]:
            return nums[0]
        
        while l <= r:
            mid = l + (r-l)//2
            print(mid)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            else:
                #pivot on the right?
                if nums[mid] < nums[l]:
                    r = mid-1 
                else:
                    l = mid+1 
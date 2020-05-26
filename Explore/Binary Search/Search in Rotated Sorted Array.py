#Two pass binary search
#Time: O(logn)
#Space: O(1)
class Solution:
    def findPivot(self,nums):
        l = 0 
        r = len(nums) - 1
        
        if nums[l] < nums[r]:
            return 0
        
        while l <= r:
            mid = (l+r)//2
            print(mid)
            if nums[mid] > nums[mid+1]:
                return mid + 1
            else:
                if nums[mid] < nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
                        
    def searchArray(self ,l, r, nums, target):
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
                
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return -1
                
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        
        pivot = self.findPivot(nums)
        
        if pivot == 0:
            return self.searchArray(0, len(nums)-1, nums, target)
        
        else:
            if target < nums[0]:
                return self.searchArray(pivot, len(nums)-1, nums, target)
            else:
                return self.searchArray(0, pivot, nums, target)
 



#One pass binary search
#Time: O(logn)
#Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        l = 0 
        r = len(nums) - 1
        
        while l <= r:
            mid = (l+r)//2
            print(mid)
            if nums[mid] == target:
                return mid
                
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

        
 


        
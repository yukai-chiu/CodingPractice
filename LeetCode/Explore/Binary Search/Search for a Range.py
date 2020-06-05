#My first try
class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            return [0,0] if nums[0] == target else [-1,-1]
        l = 0
        r = len(nums)-1
        result = [-1,-1]
        if nums[0] == target:
            result[0] = 0
        if nums[-1] == target:
            result[1] = len(nums)-1
        while l <=r:
            mid = l + (r-l)//2
 
            if nums[mid] == target and nums[mid-1] < target:
                result[0] = mid
                
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        l = 0
        r = len(nums)-1
        while l <=r:
            mid = l + (r-l)//2
            print(mid)
            if nums[mid] == target:
                if mid+1 < len(nums):
                    if nums[mid+1] > target:
                        result[1] = mid 
                else:
                    result[1] = mid 
            
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
                       
        print(result)    
        return result
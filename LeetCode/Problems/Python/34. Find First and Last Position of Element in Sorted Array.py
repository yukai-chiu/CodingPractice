#Time: O(logn)
#Space: O(1)
class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            return [0,0] if nums[0] == target else [-1,-1]
        
        result = [-1,-1]
        
        def searchEdge(left):
            l = 0 
            r = len(nums)
            
            while l <r:   
                mid = l + (r-l)//2
                if nums[mid] > target or (left and nums[mid] == target):
                    r = mid 
                else:
                    l = mid + 1
                    
            if left:
                if l < len(nums) and nums[l] == target:
                    return l
                else:
                    return -1
                
            else:
                return l-1
        
  
        result[0] = searchEdge(True)
        if result[0] == -1:
            return result
        
        
        result[1] = searchEdge(False)

        
       
        return result
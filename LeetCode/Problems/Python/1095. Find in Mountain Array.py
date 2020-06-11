#Binary search
#Time: O(logn)
#Space: O(1)


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        l = 0
        r = mountain_arr.length()-1
        #find i first, and find target in left, then right
        #if can't find in both, return -1
        
        while l < r:
            mid = l + (r-l)//2
            
            if mountain_arr.get(mid) > mountain_arr.get(mid+1):
                r = mid 
            else:
                l = mid + 1
        mount = l

        #find in left
        l = 0
        r = mount        
        
        while l <= r:
            mid = l + (r-l)//2
            if mountain_arr.get(mid) ==target:
                return mid
            elif mountain_arr.get(mid) < target:
                l = mid + 1
            else:
                r = mid - 1
                
                
        #find in right
        l = mount
        r = mountain_arr.length()-1  
        while l <= r:
            mid = l + (r-l)//2
            if mountain_arr.get(mid) ==target:
                return mid
            elif mountain_arr.get(mid) < target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
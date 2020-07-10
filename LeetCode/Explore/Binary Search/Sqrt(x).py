#Newton's
#Time: O(logn)
#Space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        x0 = x
        x1 = (x0 + x/x0)/2
        
        while abs(x0-x1) >=1:
            x0 = x1
            x1 = (x0 + x/x0)/2
        
        return int(x1)

        
#binary search
#Time: O(logn)
#Space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l = 0
        r = x//2
        while l <= r:
            mid = l + (r-l)//2
            if mid**2 <= x and (mid+1)**2 > x:
                return mid
            elif mid**2 > x:
                r = mid - 1
            else:
                l = mid + 1


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l = 0
        r = x//2
        while l <= r:
            mid = l + (r-l)//2
            
            if mid**2 > x:
                r = mid - 1
            elif mid**2 < x:
                l = mid + 1
            else:
                return mid
        
        return r
        
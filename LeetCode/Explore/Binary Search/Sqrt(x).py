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
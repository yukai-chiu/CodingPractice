class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        l = 0
        r = num//2
        while l <= r:
            mid = l + (r-l)//2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                l = mid+1
            else:
                r = mid-1
        return False
        
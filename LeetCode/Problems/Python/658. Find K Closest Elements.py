#Time: O(logn + k)
#Space: O(k)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if not arr:
            return []
        
        if len(arr) == 1:
            return arr
        
        lo = 0
        hi = len(arr) -1
        
        while lo < hi:
            
            mid = lo + (hi-lo)//2
            if arr[mid] > x:
                hi = mid
            else:
                lo = mid + 1
        if arr[lo] == x:
            pt1 = lo-1
            pt2 = lo+1
            k-=1
        else:
            pt1 = lo-1
            pt2 = lo
        
        while pt1 >=0 and pt2 < len(arr) and k > 0:
            if abs(arr[pt1] - x) > abs(arr[pt2] - x):
                pt2+=1
            else:
                pt1-=1
            k-=1
        
        while pt1 >=0 and k > 0:
            pt1-=1
            k-=1
        while pt2 < len(arr) and k > 0:
            pt2+=1
            k-=1    
 
        return arr[pt1+1:pt2]
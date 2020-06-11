#Binary search
#Time: O(logn)
#Space: O(1)
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not A:
            return -1
        
        l = 0
        r = len(A) -1
        #we want to find the peek
        while l < r:
            mid = l + (r-l)//2
            #if mid is larger than it's right, mid can possibly be the peek
            #so we want to include it
            if A[mid] > A[mid+1]:
                r = mid
            #if mid is smaller, we are safe to say that mid is not the peek
            #we can take a step
            #when l == r, l is the peek
            else:
                l = mid+1
        return l
            
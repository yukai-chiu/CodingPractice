class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        lo = 0
        hi = len(A)-1
        
        ans = -1
        while lo < hi:
            sum = A[lo] + A[hi]
            if sum >= K:
                hi-=1
            else:
                ans = max(ans, sum)
                lo+=1
        return ans
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if not heights:
            return 0 
        ref = sorted(heights)
        ans = 0
        for i in range(len(ref)):
            if ref[i] != heights[i]:
                ans +=1
        return ans
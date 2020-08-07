#brute force
#TLE
#Time: O(n^2)
#Space: O(1)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #brute force
        if not heights:
            return 0
        
        area = 0
        N = len(heights)
        for i in range(N):
            temp = float('inf')
            for j in range(i, N):
                temp = min(temp, heights[j])
                area = max(area, (j-i+1)*temp)
        return area
#Stack
#Time: O(n)
#Space: O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        area = 0
        
        stack = [-1]
        heights.append(0)
        
        for i in range(len(heights)):
            #maintain accending order
            while heights[i] < heights[stack[-1]]:
                #pop and calculate area
                h = heights[stack.pop()]
                #right bound: i-1
                #left bound: stack[-1]
                w = i-1 - stack[-1]
                area = max(area, h*w)
            stack.append(i)
        return area

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


#Better Histogram + stack
#Time: O(mn)
#Space: O(n)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        area = 0
        M = len(matrix)
        N = len(matrix[0])
        histogram = [0] * (N+1)
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == '1':
                    if j == 0 and i == 0: 
                        histogram[j] = 1
                    else:
                        histogram[j] = histogram[j] + 1
                else:
                    histogram[j] = 0
            stack = [-1]
            for k in range(N+1):
                while histogram[k] < histogram[stack[-1]]:
                    h = histogram[stack.pop()]
                    w = k-1 - stack[-1]
                    area = max(area, h*w)
                stack.append(k)
                
        
        return area
                    
                

#Histogram + stack
#Time: O(mn)
#Space: O(mn)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        area = 0
        M = len(matrix)
        N = len(matrix[0])
        histogram = [[0] * N for _ in range(M+1)]
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == '1':
                    if j == 0: 
                        histogram[i][j] = 1
                    else:
                        histogram[i][j] = histogram[i][j-1] + 1
        
        #solve for each col
        for j in range(N):
            stack = [-1]
            for i in range(M+1):
                while histogram[i][j] < histogram[stack[-1]][j]:
                    h = histogram[stack.pop()][j]
                    w = i-1 - stack[-1]
                    area = max(area, h*w)
                stack.append(i)
        return area
                    
                
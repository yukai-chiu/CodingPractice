#My first try
#Brute force with memo
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #brute force
        #traverse the matrix
        #if it is 1, find edge by go right and down, compare for the minimum
        #if it is larger than 1, find in the area
        
        def checkArea(i,j,edge):
            for row in range(edge):
                for col in range(edge):
                    #print(i+row,j+col, matrix[i+row][j+col],edge)
                    if i+row >= len(matrix) or j+col >= len(matrix[0]) or matrix[i+row][j+col] !="1":
                        return False
            return True

            
        if not matrix:
            return 0
        max_area = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] =="1":
                    #start to find edge
                    
                    col = j
                    row = i
                    while col < len(matrix[0]) and matrix[i][col] =="1":
                        col+=1
                    while row < len(matrix) and matrix[row][j] =="1":
                        row+=1
                    
                    edge = min(row-i,col-j)
                    print(edge)
                    if edge >= 1:
                        if edge > dp[i][j]:
                            #find in the area
                            for e in range(dp[i][j]+1,edge+1):
                                if checkArea(i,j,e):
                                    max_area = max(max_area,e**2)
                                    for row in range(e):
                                        for col in range(e):
                                            dp[i+row][j+col] = e
            
        return max_area                 



#Dynamic Programming
#Time: O(n*m)
#Space: O(n*m)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0
        
        max_size = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] =="1":
                    if i==0 or j==0:
                         dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    max_size = max(max_size, dp[i][j])
                   
        return max_size**2                 

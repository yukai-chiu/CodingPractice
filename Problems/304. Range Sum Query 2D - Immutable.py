class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        if not matrix or not matrix[0]:
            return
        
        self.matrix = matrix
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])-1):
                self.matrix[i][j+1] = self.matrix[i][j] + matrix[i][j+1]  
        for i in range(1,len(matrix)):
            self.matrix[i] = [a + b for a, b in zip(self.matrix[i], self.matrix[i-1])]
        print(self.matrix)                  
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2][col2] - (self.matrix[row1-1][col2] if row1 > 0 else 0) - (self.matrix[row2][col1-1] if col1>0 else 0) + (self.matrix[row1-1][col1-1] if (row1 >0 and col1 > 0) else 0)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


#Extend the matrix for more general coding
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        if not matrix or not matrix[0]:
            return
        self.matrix = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.matrix[i+1][j+1] = self.matrix[i+1][j] + self.matrix[i][j+1] + matrix[i][j] - self.matrix[i][j] 


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.matrix[row2+1][col2+1]
        b = self.matrix[row1][col2+1]
        c = self.matrix[row2+1][col1]
        d = self.matrix[row1][col1]
        return a - b - c + d 
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
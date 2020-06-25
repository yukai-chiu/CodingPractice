class Solution:
    def n_queen(self, grid, row, n):
        if row == n:
            self.result+=1
        
        def place_queen(row, i):
        
            #vertical
            for j in range(row):
                if not grid[j][i]:
                    return False
            #diagonal
            k=0
            for j in range(row, -1, -1):

                if (i-k >= 0 and not grid[j][i-k]) or (i+k < n and not grid[j][i+k]):
                    return False
                k+=1
            
            return True
            
            
        for i in range(n):
            if place_queen(row, i):
                grid[row][i] = False
                self.n_queen(grid, row+1, n)
                grid[row][i] = True
       
            
    def totalNQueens(self, n: int) -> int:
        if not n:
            return 0
        self.result = 0
        
        grid = [[True] * n for _ in range(n)]

        self.n_queen(grid,0, n)
        
        
        return self.result
class Solution:
    def backtracking(self, grid, row, n, result):
        if row == n:
            temp = deepcopy(grid)
            for i in range(n):
                temp[i] = "".join(temp[i])
            result.append(temp)
            return
        else:
            def checkValid(row, i):
                #check current col i
                for j in range(row-1,-1,-1):
                    if grid[j][i] == 'Q':
                        return False

                #check diagonal
                k=1
                for j in range(row-1,-1,-1):
                    if i+k < n and grid[j][i+k] == 'Q':
                        return False
                    if i-k >=0 and grid[j][i-k] == 'Q':
                        return False
                    k+=1

                return True


            for i in range(n):
                if checkValid(row,i):
                    grid[row][i] = 'Q'
                    self.backtracking(grid, row+1, n, result)
                    grid[row][i] = '.'

        
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n:
            return []
        
        result = []
        grid = [['.'] * n for _ in range(n)]
        
        self.backtracking(grid, 0, n, result)
        
        return result
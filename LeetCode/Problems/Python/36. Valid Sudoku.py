#First try brute force
#Time: O(1)
#Space: O(1)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False
        
        #check row
        for row in board:
            lookUp = set()
            for i in range(9):
                if row[i] != '.':
                    if row[i] not in lookUp:
                        lookUp.add(row[i])
                    else:
                        return False

        #check col
        for col in zip(*board):
            lookUp = set()
            for i in range(9):
                if col[i] != '.':
                    if col[i] not in lookUp:
                        lookUp.add(col[i])
                    else:
                        return False
        
        #check boxes
        for b_i in range(0,9,3):
            for b_j in range(0,9,3):
                lookUp = set()
                for i in range(3):
                    for j in range(3):
                        if board[b_i+i][b_j+j] != '.':
                            if board[b_i+i][b_j+j] not in lookUp:
                                lookUp.add(board[b_i+i][b_j+j])
                            else:
                                return False
        
        return True
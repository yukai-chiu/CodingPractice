#DFS + Backtracking
#Time: O(n * 4^L), L is the length of word
#Space: O(n)
class Solution:
    def dfs(self, board, row, col, word, visited, idx):
        if idx == len(word):
            return True      
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for d in directions:
            if 0 <= row + d[0] < len(board) and 0 <= col + d[1] < len(board[0]):
                new_i = row + d[0]
                new_j = col + d[1]
                if board[new_i][new_j] == word[idx] and not visited[new_i][new_j]:
                    visited[new_i][new_j] = True
                    ret = self.dfs(board, new_i, new_j, word, visited, idx+1)
                    if ret:
                        return True
                    visited[new_i][new_j] = False
        return False
                            
                            
                        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        #intuition is we can traverse the board using dfs with a visited map to perform backtracking
        #we can look at 4 neighbors
        if not board or not word:
            return False
        
        visited = [[False] * len(board[0]) for _ in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    print("in:", i,j )
                    visited[i][j] = True
                    ret = self.dfs(board, i, j, word, visited, 1)
                    if ret:
                        return True
                    else:
                        visited[i][j] = False
    
        
        
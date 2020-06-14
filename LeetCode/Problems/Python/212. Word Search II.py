#DFS + Backtracking
#Time: O(m * 4 * 3^(L-1)), m is the cells of the board, and L is the max length of words,
#4 is the first 4 directions, following is 3^(L-1) to traverse
#Space: O(n) for trie
class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = None
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        
        #construct trie
        root = TrieNode()
        for w in words:
            curr = root
            for c in w:
                curr = curr.child.setdefault(c, TrieNode())
            curr.word = w
        
        #dfs the board
        #with backtracking
        def backTracking(row, col, trie):
            letter = board[row][col]
            currNode = trie.child[letter]
            direction = [[0,1], [1,0], [0,-1], [-1,0]]
            if currNode.word != None:
                result.append(currNode.word)
                currNode.word = None
            
            board[row][col] = '#'
            
            for d in direction:
                new_r = row + d[0]
                new_c = col + d[1]
                if 0<= new_r < len(board) and 0<=new_c< len(board[0]) and board[new_r][new_c] in currNode.child:
                    backTracking(new_r, new_c, currNode)
            
            board[row][col] = letter
            #prune the trie for better performance
            if not currNode.child:
                trie.child.pop(letter)
            
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        result = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.child:
                    backTracking(i, j, root)
   
        return result
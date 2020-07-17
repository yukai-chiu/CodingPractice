//Time: O(m*n*4^L)
//Space: O(L)
class Solution {
public:
    bool dfs(int i, int j, vector<vector<char>>& board, vector<vector<bool>>& visited, string& word, int idx) {
        if(idx==word.size())
            return true;
        int M = board.size();
        int N = board[0].size();
        if(i >= M || i < 0 || j >= N || j < 0) return false;
        
        if(board[i][j] == word[idx]){
            board[i][j] = '#';
            if(dfs(i+1, j, board, visited, word, idx+1)) return true;
            if(dfs(i-1, j, board, visited, word, idx+1)) return true;
            if(dfs(i, j+1, board, visited, word, idx+1)) return true;
            if(dfs(i, j-1, board, visited, word, idx+1)) return true;
            board[i][j] = word[idx];
        }
        return false;
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        if(!board.size()) return false;
        
        int M = board.size();
        int N = board[0].size();
        
        vector<vector<bool>> visited(M, vector<bool>(N, false));
        
        for(int i=0;i<M;i++){
            for(int j=0;j<N;j++){
                if(board[i][j] == word[0]){
                    if(dfs(i, j, board, visited, word, 0))
                        return true;      
                }
            }
        }
        return false;
    }
};


class Solution {
public:
    bool dfs(int i, int j, vector<vector<char>>& board, vector<vector<bool>>& visited, string& word, int idx) {
        if(idx==word.size())
            return true;
        int M = board.size();
        int N = board[0].size();
        vector<vector<int>> direction = {{1,0}, {0,1}, {-1,0}, {0,-1}};
        
        for(vector<int> d: direction){
            int new_i = i+d[0];
            int new_j = j+d[1];
            if(new_i >=0 && new_i < M && new_j >=0 && new_j < N){
                if(!visited[new_i][new_j] && board[new_i][new_j] == word[idx]){
                    visited[new_i][new_j] = true;
                    if(dfs(new_i, new_j, board, visited, word, idx+1))
                        return true;
                    visited[new_i][new_j] = false;
                    
                }
            }
        }
        return false;
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        if(!board.size()) return false;
        
        int M = board.size();
        int N = board[0].size();
        
        vector<vector<bool>> visited(M, vector<bool>(N, false));
        
        for(int i=0;i<M;i++){
            for(int j=0;j<N;j++){
                if(board[i][j] == word[0]){
                    visited[i][j] = true;
                    if(dfs(i, j, board, visited, word, 1))
                        return true;
                    visited[i][j] = false;
                }
            }
        }
        return false;
    }
};
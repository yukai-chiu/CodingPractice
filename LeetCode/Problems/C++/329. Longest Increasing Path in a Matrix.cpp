//Time: O(mn)
//Space: O(mn)
class Solution {
public:
    int dfs(int i, int j, vector<vector<int>>& matrix, vector<vector<int>>& memo){
        int M = matrix.size();
        int N = matrix[0].size();
        if(memo[i][j] != 0) return memo[i][j];
        
        vector<vector<int>> direction = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        //check if we can start a path
        for(vector<int> d:direction){
            int new_i = i+d[0];
            int new_j = j+d[1];
            if(new_i >=0 && new_i < M && new_j>=0 && new_j < N){
                if(matrix[new_i][new_j] > matrix[i][j]){
                    memo[i][j] = max(memo[i][j], dfs(new_i, new_j, matrix, memo));
                }   
            }
        }
     
        
        return ++memo[i][j];
        
    }
    
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if(!matrix.size()) return 0;
        
        int M = matrix.size();
        int N = matrix[0].size();
        int longest = 0;
        vector<vector<int>> memo(M, vector<int>(N,0));
        for(int i=0;i<M;i++)
            for(int j=0;j<N;j++)
               longest = max(longest, dfs(i,j, matrix, memo));
        return longest;
    }
};
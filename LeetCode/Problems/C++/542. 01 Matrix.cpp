class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        if(!matrix.size()) return {};
        int M = matrix.size();
        int N = matrix[0].size();
        
        vector<vector<int>> distance(M, vector<int>(N,INT_MAX));
        queue<pair<int,int>> bfs_q;
        for(int i=0;i<M;i++)
            for(int j=0;j<N;j++)
                if(matrix[i][j]==0){
                    bfs_q.push({i,j});
                    distance[i][j] = 0;
                }
                    
        
        while(!bfs_q.empty()){
            int row = bfs_q.front().first;
            int col = bfs_q.front().second;
            bfs_q.pop();
            if(row+1 < M && distance[row][col]+1 < distance[row+1][col]){
                distance[row+1][col] = distance[row][col]+1;
                bfs_q.push({row+1,col});
            }
            if(row-1 >=0 && distance[row][col]+1 < distance[row-1][col]){
                distance[row-1][col] = distance[row][col]+1;
                bfs_q.push({row-1,col});
            }
            if(col+1 < N && distance[row][col]+1 < distance[row][col+1]){
                distance[row][col+1] = distance[row][col]+1;
                bfs_q.push({row,col+1});
            }
            if(col-1 >=0 && distance[row][col]+1 < distance[row][col-1]){
                distance[row][col-1] = distance[row][col]+1;
                bfs_q.push({row,col-1});
            }
        }
        
        return distance;
    }
};
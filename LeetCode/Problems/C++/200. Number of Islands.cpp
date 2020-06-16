class Solution {
public:
    void bfs(int i, int j, vector<vector<char>>& grid, int* visited, int M, int N){
        queue<pair<int, int>> neighbor;
        neighbor.push({i,j});
        int r, c;

        
        while(!neighbor.empty()){
            r = neighbor.front().first;
            c = neighbor.front().second;
            neighbor.pop();
            
            if(r-1 >= 0 && grid[r-1][c] == '1' && !visited[(r-1)*N+c]){
                visited[(r-1)*N+c] = 1;
                neighbor.push({r-1,c});
                }
            if(r+1 < M && grid[r+1][c] == '1' && !visited[(r+1)*N+c]){
                visited[(r+1)*N+c] = 1;
                neighbor.push({r+1,c});
                }
            if(c-1 >= 0 && grid[r][c-1] == '1' && !visited[r*N+c-1]){
                visited[r*N+c-1] = 1;
                neighbor.push({r,c-1});
                }
            if(c+1 < N && grid[r][c+1] == '1' && !visited[r*N+c+1]){
                visited[r*N+c+1] = 1;
                neighbor.push({r,c+1});
                }
        }
        
    }
    int numIslands(vector<vector<char>>& grid) {
        if(!grid.size()) return 0;
        
        int M = grid.size();
        int N = grid[0].size();
        int* visited = new int[M*N]();
        int island = 0;
        for(int i=0;i<M;i++){
            for(int j=0;j<N;j++){
                if(grid[i][j]=='1' && !visited[i*N + j]){
                    bfs(i,j, grid, visited, M, N);
                    island++;
                }
            }
        }
        return island;
    }
};
class Solution {
public:
    int dfs(vector<vector<int>>& grid, int i, int j, bool* visited, unordered_set<string>& island) {
        stack<pair<int, int>> dfs_stack;
        int M = grid.size();
        int N = grid[0].size();
        int new_i, new_j;
        visited[i*N+j] = true;
        dfs_stack.push({i,j});
        string curr_island = "";

        while(!dfs_stack.empty()){
            new_i = dfs_stack.top().first;
            new_j = dfs_stack.top().second;
            dfs_stack.pop();
            curr_island.append(to_string(new_i-i));
            curr_island.append(to_string(new_j-j));
            
            if(new_i+1 < M && grid[new_i+1][new_j] == 1 && !visited[(new_i+1)*N+new_j])
            {
                dfs_stack.push({new_i+1,new_j});
                visited[(new_i+1)*N+new_j] = true;
            }
            if(new_j+1 < N && grid[new_i][new_j+1] == 1 && !visited[new_i*N+new_j+1])
            {
                dfs_stack.push({new_i,new_j+1});
     
                visited[new_i*N+new_j+1] = true;
            }
            if(0 <= new_i-1 && grid[new_i-1][new_j] == 1 && !visited[(new_i-1)*N+new_j])
            {
                dfs_stack.push({new_i-1,new_j});
   
                visited[(new_i-1)*N+new_j] = true;
            }
            if(0<= new_j-1 && grid[new_i][new_j-1] == 1 && !visited[new_i*N+new_j-1])
            {
                dfs_stack.push({new_i,new_j-1});
      
                visited[new_i*N+new_j-1] = true;
            }

        }
       
        if(island.find(curr_island) != island.end()){
            return 0;
        }
        else{
            island.insert(curr_island);
            cout<< "new island: " << curr_island << endl;
            return 1;
        }
        
    }
    
    int numDistinctIslands(vector<vector<int>>& grid) {
        if(!grid.size()) return 0;
        
        int M = grid.size();
        int N = grid[0].size();
        bool* visited = new bool[M*N]{};
        int islands = 0;
        unordered_set<string> island;
        
        for(int i=0;i<M;i++){
            for(int j=0;j<N;j++){
                if(grid[i][j]==1 && !visited[i*N+j]){
                    islands += dfs(grid, i, j, visited, island);
                }
            }
        }
        
        return islands;
    }
};
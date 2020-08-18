class Solution {
public:
    bool checkValid(vector<int> queens, int i, int n){
        //check vertical
        for(auto y:queens){
            if(i==y) return false;
        }
        
        //check diagonal
        int offset = 1;
        for(int j=queens.size()-1;j>=0;j--){
            if((i+offset < n && queens[j] == i+offset) || (i-offset >=0 && queens[j] == i-offset))
                return false;
            offset++;
        }

        return true;
    }
    
    
    void backtracking(int& result, int row, int n, vector<int> queens) {
        if(queens.size() == n){
            //construct answer 
            result++;
            return;
        }
        
        
        for(int i=0;i<n;i++){
            if(checkValid(queens, i, n)){
                //place queens
                queens.push_back(i);
                //backtracking
                backtracking(result, row+1, n, queens);
                //reset queens
                queens.pop_back();
            }
                
        }
        
        
    }
    int totalNQueens(int n) {
        if(!n) return {};
        
        int result = 0;
        
        backtracking(result, 0, n, {});
        
        return result;
    }
};



class Solution {
public:
    bool canPlace(const int& row,const int& col, const int& n, const  vector<vector<bool>>& grid){
      
        for(int i=0;i<row;i++)    
            if(grid[i][col] == true) return false;
        
        
        for(int i=0;i<=max(col,row);i++){
            if(col-i >=0 && row-i >=0 && grid[row-i][col-i] == true) return false;
            if(col+i < n && row-i >=0 && grid[row-i][col+i] == true) return false;
        }
        
        return true;
        
    }
    bool placeQueen(int row, const int& n, vector<vector<bool>>& grid, int& count){
        if(row == n) {
            count++;
            return true;
        }
        
        for(int i=0;i<n;i++){
            
            if(canPlace(row,i, n, grid)){
                //set to true
                grid[row][i] = true;
                //recursive
                placeQueen(row+1, n, grid, count);
                //backtrack
                grid[row][i] = false;
            }
        }
        return false;
    }
    int totalNQueens(int n) {
        if(!n) return 0;
        
        
        int count =0;
        vector<vector<bool>> grid;
        grid.resize(n);
        for(int i=0;i<n;i++)
            grid[i].resize(n);
        
        
        placeQueen(0, n, grid, count);
        
        
        return count;
    }
    
};
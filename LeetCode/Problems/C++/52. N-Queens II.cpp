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
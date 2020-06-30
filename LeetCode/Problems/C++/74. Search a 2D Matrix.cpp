class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(!matrix.size() || !matrix[0].size()) return false;
    
        //search for which row
        int lo = 0;
        int hi = matrix.size()-1;
        int mid;
        while(lo <= hi){
            mid = lo + (hi-lo)/2;
            if (matrix[mid][0] == target)
                return true;
            else if(matrix[mid][0] < target)
                lo = mid+1;
            else if(matrix[mid][0] > target)
                hi = mid-1;
        }
        
        int row = hi;
        
        if(row == -1 || row >= matrix.size()) return false;
        
        //search in the row
        lo = 0;
        hi = matrix[0].size()-1;
        
        while(lo <= hi){
            mid = lo + (hi-lo)/2;
            if (matrix[row][mid] == target)
                return true;
            else if(matrix[row][mid] < target)
                lo = mid+1;
            else
                hi = mid-1;
        }
        return false; 
    }
};
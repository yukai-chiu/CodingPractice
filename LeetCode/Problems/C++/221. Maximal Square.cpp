//Time: O(mn)
//Space: O(mn)
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if(!matrix.size()) return 0;
        int area = 0;
        int M = matrix.size();
        int N = matrix[0].size();
        vector<vector<int>> count_square{};
        count_square.resize(M);
        
        for(int i=0;i<M;i++){
            count_square[i].resize(N);
            for(int j=0;j<N;j++){
                if(matrix[i][j]=='1'){
                    if(i==0 || j==0) count_square[i][j] = 1;
                    else{
                        count_square[i][j] = min(count_square[i-1][j], count_square[i][j-1]);
                        count_square[i][j] = min(count_square[i][j], count_square[i-1][j-1])+1;
                    }
                    area = max(area, count_square[i][j]);
                        
                }
            }
        }
        
        return area*area;
    }
};
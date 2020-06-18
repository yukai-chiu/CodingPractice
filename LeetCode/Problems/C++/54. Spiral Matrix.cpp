//Time: O(n)
//Space: O(n)
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if(!matrix.size()) return {};
        
        int M = matrix.size();
        int N = matrix[0].size();
        int length = M*N, step = 0, i = 0, j = 0, d = 0;
        bool* visited = new bool[length]{};
        vector<pair<int,int>> direction = {{0,1},{1,0},{0,-1}, {-1,0}};
        vector<int> ret;
        
        while(step < length){ 
            if(0<=i && i <M && 0<=j && j<N && !visited[i*N+j])
            {
                ret.push_back(matrix[i][j]);    
                step++;
                visited[i*N+j] = true;
            }
            else{
                i -= direction[d].first;
                j -= direction[d].second;
                d = (d+1)%4;
            }
            i += direction[d].first;
            j += direction[d].second;       
        }
        return ret;
    }
};
//Time: O(n)
//Space: O(1)
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if(!matrix.size()) return {};
        
        int M = matrix.size();
        int N = matrix[0].size();

        int c_l = 0, r_l = 0;
        int c_r = N-1, r_r = M-1;
        vector<int> ret;
        //four corner
        while(c_l <= c_r && r_l <= r_r){ 
            //right
            for(int c=c_l;c<=c_r;c++){
                ret.push_back(matrix[r_l][c]);
            }
            //down
            for(int r=r_l+1;r<=r_r;r++){
                ret.push_back(matrix[r][c_r]);
            }
            if(c_r > c_l && r_r > r_l){
                //left
                for(int c=c_r-1;c>c_l;c--){
                    ret.push_back(matrix[r_r][c]);
                }
                //up
                for(int r=r_r;r>r_l;r--){
                    ret.push_back(matrix[r][c_l]);
                }
            }
            
            c_l++;
            r_l++;
            c_r--;
            r_r--;
            cout << c_l <<" "<< c_r <<" "<< r_l <<" "<< r_r <<endl;
        }
        return ret;
    }
};
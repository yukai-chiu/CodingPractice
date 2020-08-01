class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        if(!A.size() || !B.size()) return {};
        vector<vector<int>> result(A.size(), vector<int>(B[0].size(), 0));
        
        unordered_map<int, unordered_map<int,int>> map_a;
        unordered_map<int, unordered_map<int,int>> map_b;
        
        
        for(int i=0;i<B.size();i++){
            for(int j=0;j<B[0].size();j++){
                if(B[i][j]!=0)
                    map_b[i][j] = B[i][j];
            }
        }

        for(int i=0;i<A.size();i++){
            for(int j=0;j<A[0].size();j++){
                if(A[i][j]!=0){
                    for(auto it=map_b[j].begin();it!=map_b[j].end();it++)
                        result[i][it->first] +=  A[i][j] * it->second;
                }  
            }
        }
        return result;  
    }
};
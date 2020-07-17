//Time:(C(9,k)) => 9!/k!(9-k)!, could be O(1) since k < 9
//Space: O(k)
class Solution {
public:
    void comb(int k, int n, int start, vector<vector<int>>& result, vector<int>& curr) {
        if(k==0 && n==0){
            result.push_back(curr);
            return;
        }
        if(k==0) return;
        
        for(int i=start;i<=9;i++){
            curr.push_back(i);
            comb(k-1, n-i, i+1, result, curr);
            curr.pop_back();
        }
        
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        if(k<0) return {};
        
        vector<vector<int>> result;
        vector<int> curr;
        comb(k, n, 1, result, curr);
        return result;
    }
};
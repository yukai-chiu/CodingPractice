//Time complexity is O(N^target) where N is a length of candidates array.
//Space complexity is O(target). if the smallest candidate is 1, the recursion will go up to target depth

class Solution {
public:
    void searchComb(vector<int>& candid, int idx, int target, vector<int>& curr, vector<vector<int>> &result) {
        if(target == 0){
            result.push_back(curr);
        }
        if(target < 0) return;
        
        for(int i=idx;i<candid.size();i++){
            curr.push_back(candid[i]);
            searchComb(candid, i, target-candid[i], curr, result);
            curr.pop_back();
        }   
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        if(!candidates.size()) return {};
        
        vector<vector<int>> result;
        vector<int> curr;
        searchComb(candidates, 0, target, curr, result);
        return result;
        
    }
};
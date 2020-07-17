//Time: O(2^n)
//Space: O(n)
class Solution {
public:
    void comb(vector<int>& candidates, int idx, int target, vector<int>& curr, vector<vector<int>>& result) {
         if(target == 0){
            result.push_back(curr);
            return;
        }
        if(target < 0) return;
       
        for(int i=idx;i<candidates.size();i++){
            if(i==idx || candidates[i]!=candidates[i-1]){
                curr.push_back(candidates[i]);
                comb(candidates, i+1, target-candidates[i], curr, result);   
                curr.pop_back();
            }
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        if(!candidates.size()) return {};
        
        vector<vector<int>> result;
        sort(candidates.begin(), candidates.end());
        vector<int> curr;
        comb(candidates, 0, target, curr, result);
        
        return result;
    }
};

class Solution {
public:
    void comb(vector<int>& candidates, int idx, int target, vector<int> curr, vector<vector<int>>& result) {
         if(target == 0){
            result.push_back(curr);
            return;
        }
        if(target < 0 || idx >= candidates.size()) return;
       
        
        curr.push_back(candidates[idx]);
        comb(candidates, idx+1, target-candidates[idx], curr, result);    
        curr.pop_back();
        idx++;
        while(idx <candidates.size() && candidates[idx]==candidates[idx-1]) idx++;
        comb(candidates, idx, target, curr, result);
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        if(!candidates.size()) return {};
        
        vector<vector<int>> result;
        sort(candidates.begin(), candidates.end());
        comb(candidates, 0, target, {}, result);
        
        return result;
    }
};
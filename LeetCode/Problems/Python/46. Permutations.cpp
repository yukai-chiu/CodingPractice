class Solution {
public:
    void backtracking(vector<int> &nums, vector<vector<int>> &ret, int first){
        if(first == nums.size()-1) {
            ret.emplace_back(nums);
            return;
        }
        for(int i=first;i<nums.size();i++){
            swap(nums[first], nums[i]);
            backtracking(nums, ret, first+1);
            swap(nums[first], nums[i]);
        }
        
    }
    vector<vector<int>> permute(vector<int>& nums) {
        if(!nums.size()) return {};
        vector<vector<int>> ret;
        
        backtracking(nums, ret, 0);
        
        
        return ret;
    }
};
class Solution {
public:
    unordered_map<int, vector<int>> lookup;
    Solution(vector<int>& nums) {
        for(int i=0;i<nums.size();i++){
            lookup[nums[i]].push_back(i);
        }

    }
    
    int pick(int target) {
        return lookup[target][rand() % (lookup[target].size())];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
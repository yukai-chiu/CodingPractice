//bit manipulation
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        if(!nums.size()) return {};
        vector<vector<int>> ret;
        int bit_count;
        bit_count = 1 << nums.size();
        for(int i=0;i<bit_count;i++){
            vector<int> cur;
            for(int j =0;j<nums.size();j++){
                if ((i>>j) & 1)
                    cur.push_back(nums[j]);
            }
            ret.push_back(cur);
        }
        return ret;
    }
};

//cascading
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        if(!nums.size()) return {};
        vector<vector<int>> ret;
        //subset(nums, 0, ret, {});
        ret.push_back({});
        for(int i=0;i< nums.size();i++){
            int result = ret.size();
            for(int j=0;j<result;j++){
                vector<int> cur =ret[j];
                cur.push_back(nums[i]);
                ret.push_back(cur);
            }
        }
        return ret;
    }
};

//backtracking
class Solution {
public:
    void subset(vector<int> &nums, int idx, vector<vector<int>>& ret, vector<int> curr, int target){
        if(curr.size() == target){
            ret.push_back(curr);
            return;
        }

        for(int i = idx; i< nums.size(); i++){
            curr.push_back(nums[i]);
            subset(nums, i+1, ret, curr, target);
            curr.pop_back();
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        if(!nums.size()) return {};
        vector<vector<int>> ret;
        for(int k=0;k<nums.size()+1;k++)
            subset(nums, 0, ret, {}, k);
   
        return ret;
    }
};
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> lookup;
        vector<int> ans;
        for(int i=0 ; i<nums.size();i++){
            if(lookup.find(target-nums[i]) == lookup.end()){
                lookup[nums[i]] = i;
            }
            else{
                ans.push_back(lookup[target-nums[i]]);
                ans.push_back(i);
                break;
            }
        }
        return ans;
    }
};


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diff;
        vector<int> v;
        for(int i = 0; i< nums.size();++i){ 
            
            if(diff.find(target - nums[i])== diff.end()){
                diff[nums[i]] = i;
            }
            else{
                v = {diff[target - nums[i]], i};
                break;
            }
        }
        return v;
    }
};
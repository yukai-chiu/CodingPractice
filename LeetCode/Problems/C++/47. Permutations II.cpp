class Solution {
public:
    bool backtracking(vector<int> nums, vector<vector<int>>& ret, int first){
        if(first == nums.size()-1){
            ret.emplace_back(nums);
            return true;
        }
        
        for(int i=first;i<nums.size();i++){
            //cout<< "first: " << first <<endl;
            if(i!=first && nums[i]==nums[first]) continue;
            
            //cout<<first << " " << nums[i] << " "<< nums[first] << endl;
            swap(nums[i], nums[first]);
            backtracking(nums, ret, first+1);
            //swap(nums[i], nums[first]);
            
        }
        return true;
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        if(nums.size()==0) return {};
        vector<vector<int>> ret;
        sort(nums.begin(),nums.end());
        backtracking(nums, ret, 0);
        
        return ret;
    }
};
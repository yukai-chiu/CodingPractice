//Time: O(n)
//Space: O(1)
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        if(!nums.size()) return {};

        vector<int> result;
        result.resize(nums.size(),1);
        int right_product = 1;

        for(int i=1;i<nums.size();i++)
            result[i] = result[i-1] * nums[i-1];
        
        
        
        for(int i=nums.size()-1;i>=0;i--){
            result[i] *= right_product;
            right_product*=nums[i];
        }
        return result;
    }
};

//Time: O(n)
//Space: O(n)
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        if(!nums.size()) return {};
        
        vector<int> front_prefix;
        vector<int> back_prefix;
        vector<int> result;
        int prefix_product = 1;
        for(int i=0;i<nums.size();i++){
            front_prefix.push_back(prefix_product);
            prefix_product*= nums[i];
        }
        prefix_product = 1;
        for(int i=nums.size()-1;i>=0;i--){
            back_prefix.push_back(prefix_product);
            prefix_product*= nums[i];
        }
        
        for(int i=0;i<nums.size();i++){
            result.push_back(front_prefix[i]*back_prefix[nums.size()-1-i]);
        }
        
        return result;
    }
};
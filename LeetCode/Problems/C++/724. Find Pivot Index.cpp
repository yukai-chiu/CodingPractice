//Prefix sum array
//Time: O(n)
//Space: O(1)
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        if(!nums.size())
            return -1;
        
        int sum = 0;
        int left_sum = 0;   
        for(int i=0;i<nums.size();i++){
            sum+=nums[i];
        }
        for(int i=0;i<nums.size();i++){
            if (left_sum == sum-left_sum-nums[i])
                return i;
            left_sum+=nums[i];
        }
        return -1;
    }
};


//Prefix sum array
//Time: O(n)
//Space: O(n)
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        if(!nums.size())
            return -1;
        
        vector<int> prefix_sum;
        int sum = 0;
        prefix_sum.push_back(sum);
        for(int i=0;i<nums.size();i++){
            sum+=nums[i];
            prefix_sum.push_back(sum);
        }
        for(int i=0;i<nums.size();i++){
            if (prefix_sum[i] == prefix_sum[nums.size()]-prefix_sum[i+1])
                return i;
        }
        return -1;
    }
};
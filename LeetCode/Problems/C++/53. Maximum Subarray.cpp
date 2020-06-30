class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(!nums.size()) return 0;
        
        int max_sum = INT_MIN;
        
        int* dp = new int[nums.size()]{};
        
        for(int i=0;i<nums.size();i++){
            if(i==0)
                dp[i] = nums[i];
            else
                dp[i] = max(dp[i-1]+nums[i], nums[i]);
            max_sum = max(max_sum, dp[i]);
        }
        return max_sum;
    }
};
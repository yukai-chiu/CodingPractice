class Solution {
public:
    int missingNumber(vector<int>& nums) {
        if(!nums.size()) return 0;
        int sum = nums.size() * (nums.size()+1)/2;
        
        for(int n:nums){
            sum-=n;
        }
        return sum;
    }
};
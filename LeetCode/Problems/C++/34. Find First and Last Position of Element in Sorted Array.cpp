class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if(!nums.size()) return {-1,-1};

        vector<int> ans = {-1,-1};
        
        int lo =0;
        int hi = nums.size();
        //find left bound
        while(lo<hi){
            int mid = lo+(hi-lo)/2;
            if(nums[mid] >= target){
                hi = mid;
            }
            else
                lo = mid+1;
        }
        
        //check if valid
        if(lo >= nums.size() || nums[lo]!=target) return ans;
        ans[0] = lo;
        
        lo =0;
        hi = nums.size();
        while(lo<hi){
            int mid = lo+(hi-lo)/2;
            if(nums[mid] > target){
                hi = mid;
            }
            else
                lo = mid+1;
        }
        ans[1] = lo-1;
        return ans;
    }
};
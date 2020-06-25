class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if(!nums.size() || nums.size()==1) return 0;
        
        int l = 0;
        int r = nums.size()-1;

        //find peak
        while(l<r){
            int mid = l + (r-l)/2;
            if(nums[mid]>nums[mid+1])
                r = mid;
            else
                l = mid+1;
        }
        
        return l;
    }
};
//704. Binary Search
class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(!nums.size()) return -1;
        
        int lo = 0;
        int hi = nums.size()-1;
        
        while(lo <= hi){
            int mid = lo + (hi-lo)/2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] > target)
                hi = mid-1;
            else
                lo = mid+1;
        }
        
        return -1;
    }
};
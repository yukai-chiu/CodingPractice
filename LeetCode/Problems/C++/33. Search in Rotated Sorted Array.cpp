class Solution {
public:
    int searchPivot(vector<int>& nums){
        if(nums.front() < nums.back()) return 0;
        int lo = 0;
        int hi = nums.size()-1;
        int mid;
        
        while(lo <= hi){
            mid = lo + (hi-lo)/2;
            if(nums[mid]>nums[mid+1])
                return mid+1;
            else if(nums[mid]>=nums[lo])
                lo = mid+1;
            else
                hi = mid-1;
        }
        return 0;
        
    }
    
    
    int search(vector<int>& nums, int target) {
        if(!nums.size()) return -1;
        
        if(nums.size()==1)
            return nums[0] == target? 0:-1;
        
        //find the pivot first
        int lo = 0;
        int hi = nums.size()-1;
        int mid;
        
        int pivot = searchPivot(nums);
        
        if(pivot == 0){
            lo = 0;
            hi = nums.size()-1;
        }
        
        //right or no pivot
        else if(target < nums[0]){

            lo = pivot;
            hi = nums.size()-1;
            cout << "right" << lo << hi;
        }
        //left
        else{
            
            lo = 0;
            hi = pivot-1;
            cout << "left" << lo << hi;
        }
            
        while(lo<=hi){
            mid = lo + (hi-lo)/2;
            if(nums[mid]==target)
                return mid;
            else if(nums[mid] > target)
                hi = mid-1;
            else
                lo = mid+1;
        }
        

        return -1;
        
        
    }
};
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if(!nums.size()) return 0;
        
        int l = 0, r = nums.size();
        while(l<r){
            if(nums[l] == val){
                nums[l] = nums[r-1]; 
                r--;
            }
            else
                l++;
        }
        
        return r;            
    }
};


class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if(!nums.size()) return 0;
        
        
        int l = 0, r = nums.size()-1;
        while(l<=r){
            if(nums[r]==val){
                r--;
            }
            else if(nums[l] == val){
                nums[l] = nums[r]; 
                r--;
                l++;
            }
            else
                l++;
            
        }
        return l;
        
            
        
    }
};
class Solution {
public:
    int partition(vector<int>& nums, int lo, int hi) {
        int pivot = nums[hi];
        int i = lo;
        int temp;
        for(int j=lo;j<hi;j++){
            if(nums[j] < pivot){
                temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                i++;
            }
        }
        nums[hi] = nums[i];
        nums[i] = pivot;
        return i;
        
        
    }
    void quickSort(vector<int>& nums, int lo, int hi) {
        if(lo<hi){
            int pivot = partition(nums, lo, hi);
            quickSort(nums, lo, pivot-1);
            quickSort(nums, pivot+1, hi);
        }
    }
    vector<int> sortArray(vector<int>& nums) {
        if(!nums.size()) return {};
        quickSort(nums,0, nums.size()-1);
        return nums;
    }
};
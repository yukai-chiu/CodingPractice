//#include <stdlib.h> 
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        if(!nums.size()) return 0;
        
        sort(nums.begin(), nums.end());
        
        int closest = INT_MAX, l, r, sum, ans;
        int N = nums.size();
        for(int i=0;i<N;i++){
            l = i+1;
            r = N-1;
            while(l<r){
                sum = nums[i] + nums[l] + nums[r];
                if(abs(target-sum) < abs(closest)){
                    closest = target-sum;   
                }
                if(sum == target) break;
                else if(sum < target) l++;
                else if(sum > target) r--;
            }
        } 
        return target-closest;
    }
};
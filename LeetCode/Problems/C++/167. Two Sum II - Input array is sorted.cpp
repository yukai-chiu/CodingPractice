class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        //two pointer
        int lo = 0, hi = numbers.size()-1;
        
        while(lo<hi){
            int sum = numbers[lo] + numbers[hi];
            if(sum==target){
                break;
            }
            else if(sum < target) lo++;
            else if(sum > target) hi--;
        }   
        return {lo+1,hi+1};
    }
};
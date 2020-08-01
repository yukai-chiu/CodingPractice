//Time: O(n)
//Space: O(n)
class Solution {
public:
    vector<int> backup;
    vector<int> num;
    int size;
    Solution(vector<int>& nums) {
        backup.assign(nums.begin(),nums.end());
        num = nums;
        size = nums.size();
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        num.assign(backup.begin(),backup.end());
        return num;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        for(int i=0;i<size;i++){
            int n = rand() % (size-i);
            int temp = num[i];
            num[i] = num[i+n];
            num[i+n] = temp;
        }
        return num;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
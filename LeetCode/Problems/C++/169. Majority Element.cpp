//Time:O(n)
//Space: O(1)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if(!nums.size()) return -1;
        
        int count = 0, candidate;
        for(int n:nums){
            if(count==0) candidate = n;
            count+= (candidate==n)? 1:-1;
        }
        return candidate;
    }
};


//Time:O(n)
//Space:O(n)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if(!nums.size()) return -1;
        
        unordered_map<int,int> count;
        for(int n:nums){
            count[n]+=1;
            if(count[n] > nums.size()/2) return n;
        }
        return -1;
    }
};
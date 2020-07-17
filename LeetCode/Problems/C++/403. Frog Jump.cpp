class Solution {
public:
    bool canCross(vector<int>& stones) {
        if(!stones.size()) return false;
        
        unordered_map<int, unordered_set<int>> dp;
        for(int i:stones){
            dp[i] = {};
        }
        
        if(dp.find(1)!=dp.end())
            dp[1].insert(1);
        else
            return false;
                
        for(int i:stones){
            for(int k:dp[i]){
                for(int step=k-1;step<k+2;step++){
                    if(step>0 && dp.find(i+step)!=dp.end()){
                        dp[i+step].insert(step);
                        if(i+step == stones.back()) return true;
                    }
                }
            }
        }
        return !dp[stones.back()].empty();
    }
};
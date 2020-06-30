class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if(!coins.size() || !amount) return 0;
        
        vector<int> dp;
       
        for(int i=0; i<=amount;i++){
            dp.push_back(INT_MAX);
        }
        dp[0] = 0;
        
        for(int i=1; i<=amount;i++){
            for(int c=0;c<coins.size();c++){
                if(i-coins[c]>=0 && dp[i-coins[c]] != INT_MAX){
                    dp[i] = min(dp[i], dp[i-coins[c]] + 1);
                }
            }
        }
        
        return dp[amount] != INT_MAX ? dp[amount] : -1;
        
    }
};
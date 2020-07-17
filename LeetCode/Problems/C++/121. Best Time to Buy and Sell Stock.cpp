class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(!prices.size()) return 0;
        
        int max_profit = 0;
        int min_price = INT_MAX;
        for(int i=0;i<prices.size();i++){
            min_price = min(min_price, prices[i]);
            max_profit = max(max_profit, prices[i]-min_price);
        }
        return max_profit;
        
    }
};


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(!prices.size()) return 0;
        
        int low = INT_MAX;
        int high = INT_MIN;
        int maxprofit = 0;
        for(int p:prices){
            if(p < low) {
                low = p;
                high = p;
            }
            if(p > high) high = p;
            maxprofit = std::max(maxprofit, high-low);
        }
        return maxprofit;
    }
};
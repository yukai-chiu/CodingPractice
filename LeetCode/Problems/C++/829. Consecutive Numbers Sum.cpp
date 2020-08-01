class Solution {
public:
    int consecutiveNumbersSum(int N) {
        if(N<=0) return 0;
        
        int upper_limit = ceil(sqrt(2*N + 0.25) - 0.5);
        int count = 0;
        
        for(int k=1;k<=upper_limit;k++){
            if((N-k*(k+1)/2) % k ==0) count++; 
        }
        return count;
        
    }
};
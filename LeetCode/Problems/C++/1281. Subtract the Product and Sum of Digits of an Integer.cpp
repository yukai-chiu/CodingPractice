class Solution {
public:
    int subtractProductAndSum(int n) {
        if(n==0) return 0;
        
        int sum = 0, prod = 1;
        
        while(n>0){
            sum+= n % 10;
            prod *= n % 10;
            n /=10;
        }
        
        return prod-sum;
    }
};
class Solution {
public:
    int getNext(int n){
        int total_sum = 0, digit;
        while(n>0){
            digit = n % 10;
            total_sum += digit * digit;
            n /=10;
        }
        return total_sum;
    }
    bool isHappy(int n) {
        unordered_set<int> seen;
        
        while(n!=1 && seen.find(n)==seen.end()){
            seen.insert(n);
            n = getNext(n);
        }
        return n==1;
    }
};
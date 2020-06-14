//Two pointers
//Time: O(n)
//Space: O(1) 
class Solution {
public:
    int twoSumLessThanK(vector<int>& A, int K) {
        sort(A.begin(), A.end());
        
        int lo = 0, hi = A.size()-1;
        int minSum = -1, sum;      
        while(lo<hi){
            sum = A[lo] + A[hi];
            if(sum >= K){
                hi--;
            }
            else{
                minSum = max(minSum, sum);
                lo++;
            }
        }
        return minSum;
    }
};
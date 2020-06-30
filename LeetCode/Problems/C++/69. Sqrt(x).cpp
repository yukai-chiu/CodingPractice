class Solution {
public:
    int mySqrt(int x) {
        if(x < 2) return x;
        
        int lo = 1;
        int hi = x/2;
        long mid;
        while(lo<=hi){
            mid = lo + (hi - lo)/2;
            if(mid*mid <= x && (mid+1)*(mid+1) > x)
                break;
            else if(mid*mid > x)
                hi = mid-1;
            else
                lo = mid+1;
        }
        
        return mid;
    }
};
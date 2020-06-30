//278. First Bad Version
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        if(!n) return 0;
        
        int lo = 0;
        int hi = n;
        int mid;
        
        while(lo < hi){
            mid = lo + (hi - lo)/2;
            if(isBadVersion(mid))
                hi = mid;
            else
                lo = mid+1;
        }
        return lo;
    }
};
class Solution {
public:
    bool isPowerOfTwo(int n) {
        bool bit = false;
        
        while(n){
            if(n&1 && !bit) bit = true;
            else if(bit) return false;
            n>>=1;
        }
        return bit;
    }
};


class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n==0) return false;
        
        long x = n;
        return (x & (x-1))==0;
    }
};
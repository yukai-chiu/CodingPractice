class Solution {
public:
    void reverseString(vector<char>& s) {
        if(!s.size()) return;
        
        int hi = s.size()-1;
        int lo = 0;
        while(lo<hi){
            swap(s[lo++], s[hi--]);
        }
    }
};
class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        if(!s.size() && !t.size()) return false;
        
        int n_s = s.size();
        int n_t = t.size();
        
        if(n_s > n_t) 
            return isOneEditDistance(t,s);
        
        if(n_t - n_s > 1) return false;
        
        int i = 0, j = 0;
        while(i < n_s){
            if(s[i]!=t[j]){
                if(n_s == n_t) return s.substr(i+1,n_s-i-1) == t.substr(j+1,n_t-j-1);
                else return s.substr(i,n_s-i) == t.substr(j+1,n_t-j);
            }
            else{
                i++;
                j++;
            }
        } 
        return n_s +1 == n_t;
    }
};
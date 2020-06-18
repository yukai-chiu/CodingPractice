class Solution {
public:
    bool isPalindrome(string s) {
        if(!s.size()) return true;
        
        int l = 0, r = s.size()-1;
        
        while(l<r){
            //find the next alnum
            while(l<r && !isalnum(s[l])) l++;
            while(l<r && !isalnum(s[r])) r--;
            
            if(tolower(s[l])!=tolower(s[r]))
                return false;
            l++;
            r--;
        }
        return true;
    }
};
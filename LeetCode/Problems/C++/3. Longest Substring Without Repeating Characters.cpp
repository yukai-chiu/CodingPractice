class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(!s.size()) return 0;
        
        unordered_map<char,int> lookup;
        int max_length = INT_MIN, start = 0;
        for(int i=0;i<s.size();i++){
            if(lookup.find(s[i])!=lookup.end()){
                start = max(start,lookup[s[i]]+1);
            }
            max_length = max(max_length, i-start+1);
            lookup[s[i]] = i;
        }
        return max_length;
    }
};
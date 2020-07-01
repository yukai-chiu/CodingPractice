class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> ana_s;
        unordered_map<char, int> ana_t;
        
        for(int i=0;i<s.size();i++)
            ana_s[s[i]]+=1;
        
        for(int i=0;i<t.size();i++)
            ana_t[t[i]]+=1;
        
        return ana_s == ana_t;
    }
};
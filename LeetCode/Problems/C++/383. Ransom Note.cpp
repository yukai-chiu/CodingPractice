class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if(!ransomNote.size() && !magazine.size()) return true;
        if(!magazine.size()) return false;
        
        unordered_map<char, int> count_m;
        
        for(char ch: magazine)
            count_m[ch]+=1;
        
        for(char ch: ransomNote)
        {
            if(count_m.find(ch) == count_m.end()) return false;
            count_m[ch]-=1;
            if(count_m[ch] <0) return false;
        }
        return true;
    }
};
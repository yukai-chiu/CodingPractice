class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        if(!words.size()) return false;
        if(words.size()==1) return true;
        
        unordered_map<char,int> lookup;
        for(int i=0;i<order.size();i++){
            lookup[order[i]] = i;
        }
        
        for(int i=0;i<words.size()-1;i++){
            string s1 = words[i];
            string s2 = words[i+1];
            int p1 = 0;
            int p2 = 0;
            while(p1<s1.size() && p2<s2.size()){
                if(s1[p1]!=s2[p2]){
                    if(lookup[s1[p1]] > lookup[s2[p2]]) return false;
                    break;
                }
                p1++;
                p2++;  
            }
            if(s1.substr(0,p1)==s2 && p1 < s1.size()) return false;
        }
        
        return true;
    }
};
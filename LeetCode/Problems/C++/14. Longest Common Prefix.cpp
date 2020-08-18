class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(!strs.size()) return "";
        int idx = 0;
        int min_length = INT_MAX;
        for(auto s:strs){
            min_length = min(min_length, (int)s.size());
        }
            
        char c;
        for(int i=0;i<min_length;i++){
            for(int j=0;j<strs.size();j++){
                if(j==0) 
                    c = strs[j][i];
                else if(strs[j][i] != c)
                    return strs[0].substr(0,i);
            }
        }
        return strs[0].substr(0,min_length);
    }
};
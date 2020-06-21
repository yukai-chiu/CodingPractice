class Solution {
public:
    void backtracking(vector<string>& result, unordered_map<char,vector<char>>& lookup, string& cur, string digits, int idx){
        if(idx==digits.size()) {
            result.push_back(cur);
            return ;
        }
        vector<char> candid = lookup[digits[idx]];
        for(int i=0; i<candid.size();i++){
            cur[idx] = candid[i];
            backtracking(result, lookup, cur, digits, idx+1);
        }

        
    }
    vector<string> letterCombinations(string digits) {
        if(!digits.size()) return {};
        vector<string> result;
        unordered_map<char,vector<char>> lookup;
        
        lookup['2'] = vector<char> {'a', 'b', 'c'};
        lookup['3'] = vector<char> {'d', 'e', 'f'};
        lookup['4'] = vector<char> {'g', 'h', 'i'};
        lookup['5'] = vector<char> {'j', 'k', 'l'};
        lookup['6'] = vector<char> {'m', 'n', 'o'};
        lookup['7'] = vector<char> {'p', 'q', 'r', 's'};
        lookup['8'] = vector<char> {'t', 'u', 'v'};
        lookup['9'] = vector<char> {'w', 'x', 'y', 'z'};
        string cur = "";
        for(int i=0;i<digits.size();i++) cur.append(" ");
        
        backtracking(result, lookup, cur, digits, 0);
        return result;
    }
};
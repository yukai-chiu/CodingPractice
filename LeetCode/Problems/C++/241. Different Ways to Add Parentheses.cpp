

class Solution {
public:
    vector<int> diffWays(string s, unordered_map<string, vector<int>>& memo){
        if(all_of(s.begin(), s.end(), ::isdigit)){
            return {stoi(s)};
        }
        
        if(memo.find(s)!=memo.end()){
            return memo[s];
        }
        
        vector<int> result;
        for(int i=0;i<s.size();i++){
            if(s[i] == '+' || s[i] == '-' || s[i] == '*'){
                vector<int> left = diffWays(s.substr(0,i), memo);
                vector<int> right = diffWays(s.substr(i+1), memo);
                for(int j=0;j<left.size();j++){
                    for(int k=0;k<right.size();k++){
                        result.push_back(helper(left[j], right[k], s[i]));
                    }
                }
            }
            
        }
        memo[s] = result;
        return memo[s];
    }
    
    int helper(int l, int r, char op){
        if(op == '+')
            return l + r;
        else if(op == '-')
            return l - r;
        else if (op == '*')
            return l * r;
        else
            return NULL;
    }
    
    
    
    vector<int> diffWaysToCompute(string input) {
        if(!input.size()) return {};
        
        vector<int> result;
        unordered_map<string, vector<int>> memo;
        result = diffWays(input, memo);
        
        return result;
    }
};
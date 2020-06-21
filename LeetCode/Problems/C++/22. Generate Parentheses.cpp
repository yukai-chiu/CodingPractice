class Solution {
public:
    void backtracking(string s, int left, int right, int n, vector<string>& result) {
        if(s.size() == 2*n) result.push_back(s);
        
        if(left < n){
            s.append("(");
            backtracking(s, left+1, right, n, result);
            s.pop_back();
        }
        if(left > right){
            s.append(")");
            backtracking(s, left, right+1, n, result);
            s.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        if(n<=0) return {};
        
        vector<string> result;
        backtracking("", 0, 0, n, result);
        
        return result;
    }
};
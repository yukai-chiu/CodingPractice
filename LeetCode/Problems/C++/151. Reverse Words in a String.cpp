class Solution {
public:
    string reverseWords(string s) {
        if(!s.size()) return "";
        
        stringstream ss(s);
        string word;
        stringstream output;
        stack<string> mystack;
        while(ss>>word){
            mystack.push(word);
            cout << word;
        }
        
        while(!mystack.empty()){
            output << mystack.top();
            mystack.pop();
            if(!mystack.empty())
                output << " ";
        }
        
        return output.str();
    }
};
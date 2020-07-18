class Solution {
public:
    bool isStrobogrammatic(string num) {
        if(!num.size()) return false;
        
        unordered_map<char, char> lookup {{'0','0'},{'1','1'},{'6','9'},{'8','8'},{'9','6'}};
        for(int i=0, j=num.size()-1;i<num.size();i++,j--){
            if(lookup.find(num[j]) == lookup.end()) return false;
            if(num[i] != lookup[num[j]]) return false; 
        }
        return true;
    }
};
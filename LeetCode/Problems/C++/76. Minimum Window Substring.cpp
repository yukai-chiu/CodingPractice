class Solution {
public:
    string minWindow(string s, string t) {
        if(!s.size() || !t.size()) return "";
        
        //construct lookup for t
        unordered_map<char, int> lookup_t;
        unordered_map<char, int> cur_window;
        for(auto i:t){
            if(lookup_t.find(i) == lookup_t.end())
                lookup_t[i] = 1;
            else 
                lookup_t[i] ++;
        }
        cout << lookup_t.size() << endl;
        int l = 0, r = 0, S = s.size();
        int found = 0;
        int min_size = INT_MAX, start, end;
        while(r < S){
            //move right pointer to find if the current window matches t
            if(r < S && found < lookup_t.size()){
                if(cur_window.find(s[r]) == cur_window.end())
                    cur_window[s[r]] = 1;
                else
                    cur_window[s[r]]++;
                
                if(lookup_t.find(s[r]) != lookup_t.end() && cur_window[s[r]] == lookup_t[s[r]]){
                    found++;
                }            
            }
            //move left pointer until we break the match
            while(l < S && found == lookup_t.size()){
                if(r-l+1 < min_size){
                    min_size = r-l+1;
                    start = l;
                    end = r;
                }
                
                cur_window[s[l]]--;
                if(lookup_t.find(s[l]) != lookup_t.end() && cur_window[s[l]] < lookup_t[s[l]]){
                    found--;
                }
                l++;
            }
            r++;
        }
        return min_size == INT_MAX ? "" : s.substr(start, min_size);
    }
};
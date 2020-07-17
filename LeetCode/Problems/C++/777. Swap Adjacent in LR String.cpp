//Two pointers
//Time: O(n)
//Space: O(1)
class Solution {
public:
    bool canTransform(string start, string end) {
        if(start.size() != end.size())
            return false;
        
        int i=0, j=0;
        
        while(i < start.size() && j < end.size()){
            while(i < start.size() && start[i] == 'X') i++;
            while(j < end.size() && end[j] == 'X') j++;
            if(start[i]!=end[j]) 
                return false;
            else if(start[i] == 'R' &&　i>j) return false;
            else if(start[i] == 'L' &&　i<j) return false;    
            
            i++;
            j++;
            
        }
        
        while(i<start.size()){
            if(start[i] == 'R' || start[i] == 'L') return false;
            i++;
        }
        
        while(j<end.size()){
            if(end[j] == 'R' || end[j] == 'L') return false;
            j++;
        }
        
        
        return true;
    }
};

//Time: O(n)
//Space: O(n)
class Solution {
public:
    bool canTransform(string start, string end) {
        if(start.size() != end.size())
            return false;
        
        vector<pair<char, int>> s1;
        vector<pair<char, int>> s2;
        for(int i=0;i<start.size();i++){
            if(start[i]=='R' || start[i] == 'L')
                s1.push_back({start[i],i});
        }
        for(int i=0;i<end.size();i++){
            if(end[i]=='R' || end[i] == 'L')
                s2.push_back({end[i],i});
        }
        
        if(s1.size()!=s2.size()) return false;
        
        for(int i=0;i<s1.size();i++){
            if(s1[i].first==s2[i].first){
                //R can only go right
                if(s1[i].first == 'R' && s1[i].second > s2[i].second)
                    return false;
                
                if(s1[i].first == 'L' && s1[i].second < s2[i].second)
                    return false;
            }
            else{
                return false;
            }
        }
        
        return true;
    }
};
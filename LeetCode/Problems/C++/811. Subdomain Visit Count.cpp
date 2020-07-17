//Time: O(n)
//Space: O(n)
class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        if(!cpdomains.size()) return {};
        
        unordered_map<string, int> count;
        vector<string> result;
        for(string s: cpdomains){
            
            int split = s.find(" ");
            int c = stoi(s.substr(0,split));
            string domain = s.substr(split+1);
            
            count[domain]+= c;
            for(int i=0;i<domain.size();i++){
                if(domain[i]=='.') 
                    count[domain.substr(i+1)]+=c;
            }
        }
          
        for(auto it=count.begin();it!=count.end();it++){
            result.push_back(to_string(it->second) + " " + it->first);
        }
        
        return result;
        
    }
};
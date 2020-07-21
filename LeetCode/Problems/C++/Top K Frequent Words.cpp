class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        if(!words.size()) return {};
        
        vector<string> result;
        result.resize(k);
        priority_queue<pair<int, string>> pq;
        unordered_map<string,int> count;
        for(string s:words){
            count[s]-=1;
        }
        
        for(auto it=count.begin();it!=count.end();it++){
            pq.push({it->second,it->first});
            if(pq.size()>k)
                pq.pop();
        }
        while(!pq.empty()){
            result[--k] = pq.top().second;
            pq.pop();
        }
        
        return result;
    }
};
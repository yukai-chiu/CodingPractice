class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if(!intervals.size()) return {};
        
        priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        for(int i=0; i<intervals.size();i++){
            pq.push({intervals[i][0],-1});
            pq.push({intervals[i][1],1});
        }
        
        vector<vector<int>> result;
        int start = 0;
        int end = 0;
        int status = 0;
        while(!pq.empty()){
            pair<int, int> cur = pq.top();
            pq.pop();
            status += cur.second;

            if(status == -1 && cur.second == -1)
                start = cur.first;

            if(status == 0){
                end = cur.first;
                result.push_back({start,end});
            } 
        }      
        return result;
    }
};
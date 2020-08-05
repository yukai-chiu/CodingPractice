//bucket
//Time: O(n)
//Space: O(n)
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        if(!trips.size()) return true;
        
        vector<int> schedule;
        schedule.resize(1001);
        for(int i=0;i<trips.size();i++){
            schedule[trips[i][1]] +=-trips[i][0];
            schedule[trips[i][2]] +=trips[i][0];
        }
        for(int i=0;i<1001;i++){
            capacity +=schedule[i];
            if(capacity < 0) return false;
        }
        return true;
    }
};

//priority queue
//Time: O(nlogn)
//Space: O(n)
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        if(!trips.size()) return true;
        
        priority_queue<pair<int, int>> schedule;
        
        for(int i=0;i<trips.size();i++){
            schedule.push({-trips[i][1], -trips[i][0]});
            schedule.push({-trips[i][2], trips[i][0]});
        }
        
        while(!schedule.empty()){
            int curr = schedule.top().second;
            schedule.pop();
            capacity+=curr;
            if(capacity < 0) return false;
        }
        
        return true;
    }
};
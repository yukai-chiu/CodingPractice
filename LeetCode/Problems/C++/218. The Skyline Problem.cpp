class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        if(!buildings.size()) return {};
        
        vector<vector<int>> critical_pt;
        
        //use long for height
        priority_queue<pair<int, long>> alive;
        vector<vector<int>> result;
        for(int i=0; i<buildings.size();i++){
            critical_pt.push_back({buildings[i][0], -buildings[i][2], buildings[i][1]});
            critical_pt.push_back({buildings[i][1], 0, 0});
        }
        sort(critical_pt.begin(), critical_pt.end());
        
        //height, right
        alive.push({0, LONG_MAX});

        
        for(int i=0; i<critical_pt.size();i++){
            //check if buildings r are smaller than i
            while(alive.top().second <= critical_pt[i][0]){
                alive.pop();
            }
            
            //check if i is the start of the new building
            if(critical_pt[i][1]!=0){
                alive.push({-critical_pt[i][1], critical_pt[i][2]});
            }
            
            //check if height change, and add to result
            if(i==0 || (result.back()[1] != alive.top().first)){
                result.push_back({critical_pt[i][0], alive.top().first});
            }
        }

        return result;
        
    }
};
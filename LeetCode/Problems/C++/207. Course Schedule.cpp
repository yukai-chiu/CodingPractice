class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        
        unordered_map<int, int> depend;
        unordered_map<int, unordered_set<int>> adj_list;
        queue<int> myqueue;
        vector<int> result;
        //initialize
        for(int i=0;i<numCourses;i++){
            depend[i] = 0;
        }
        for(int i=0;i<prerequisites.size();i++){
            depend[prerequisites[i][0]]++;
            adj_list[prerequisites[i][1]].insert(prerequisites[i][0]);    
        }
    
        for(auto it=depend.begin();it!=depend.end();++it){
            if(it->second == 0) myqueue.push(it->first);
        }
        
        while(!myqueue.empty()){
            int curr = myqueue.front();
            myqueue.pop();
            result.push_back(curr);
            for(auto it = adj_list[curr].begin();it!=adj_list[curr].end(); ++it){
                depend[*it]--;
                if(depend[*it]==0)myqueue.push(*it);
            }
        } 
        return result.size() == numCourses;
    }
    
};
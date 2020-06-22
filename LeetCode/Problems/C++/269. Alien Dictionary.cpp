class Solution {
public:
    string alienOrder(vector<string>& words) {
        if(!words.size()) return "";
        
        unordered_map<char, int> in_degree;
        unordered_map<char, unordered_set<char>> adj_list;
        string result = "";
        //step 1: build relationship/dependencies graph
        for(int i=0;i<words.size();i++){
            for(int j=0;j<words[i].size();j++){
                in_degree[words[i][j]]=0;
            }
        }
        
        for(int i=0;i<words.size()-1;i++){
            string w1 = words[i];
            string w2 = words[i+1];
            int length = min(w1.size(),w2.size());
            for(int j=0;j<length;j++){
                if(w1[j]!=w2[j]){
                    //if(in_degree.find(w2[j])==in_degree.end()){
                    //   in_degree[w2[j]] = 1;
                    //}
                    if(adj_list[w1[j]].find(w2[j]) == adj_list[w1[j]].end()){
                        in_degree[w2[j]] += 1;

                    }
                    adj_list[w1[j]].insert(w2[j]);
                    break;
                }
                //edge case when w2 is prefix of w1
                if(j==length-1 && w1[j]==w2[j] && w2.size() < w1.size()) return result;
                
            }
        }
        
        //step 2: traverse, we can pick the one with 0 indegree first(no dependency)
        queue<char> myqueue;
        
        //setup queue
        for(auto it=in_degree.begin(); it !=in_degree.end();it++){
            //cout << it->first << " " << it->second << endl;
            if(it->second == 0) myqueue.push(it->first);
        };
        
        while(!myqueue.empty()){
            char curr = myqueue.front();
            myqueue.pop();
            result+=curr;
            unordered_set<char> depend = adj_list[curr];
            for(auto it=depend.begin(); it!=depend.end();++it){
                in_degree[*it]--;
                //cout<<*it<<endl;
                if(in_degree[*it] == 0) myqueue.push(*it);
            }
        }
        
        if(result.size()!=in_degree.size()) return "";
        
        return result;
        
    }
};
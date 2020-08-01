class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if(!beginWord.size() || !endWord.size() || !wordList.size()) return 0;
        if(std::find(wordList.begin(), wordList.end(), endWord) == wordList.end()) return 0;
        
        unordered_map<string, vector<string>> graph;
        
        for(int i=0;i<wordList.size();i++){
            for(int j=0;j<beginWord.size();j++){
                graph[wordList[i].substr(0,j) + "*" + wordList[i].substr(j+1)].push_back(wordList[i]);
            }
        }
        
        unordered_set<string> visited;
        visited.insert(beginWord);
        
        queue<pair<string, int>> bfs_queue;
        bfs_queue.push({beginWord, 1});
        
        while(!bfs_queue.empty()){
            string curr = bfs_queue.front().first;
            int steps = bfs_queue.front().second;
            bfs_queue.pop();
            
            for(int i=0;i<curr.size();i++){
                vector<string> neighbor = graph[curr.substr(0,i) + "*" + curr.substr(i+1)];
                for(auto it=neighbor.begin(); it!=neighbor.end();it++){
                    if(*it==endWord) return steps+1;
                    if(visited.find(*it)==visited.end()){
                        visited.insert(*it);
                        bfs_queue.push({*it, steps+1});
                    }     
                }
            }   
        }
        return 0;
    }
};

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if(!beginWord.size() || !endWord.size() || !wordList.size()) return 0;
        if(std::find(wordList.begin(), wordList.end(), endWord) == wordList.end()) return 0;
        
        unordered_map<string, vector<string*>> graph;
        
        for(int i=0;i<wordList.size();i++){
            for(int j=0;j<beginWord.size();j++){
                graph[wordList[i].substr(0,j) + "*" + wordList[i].substr(j+1)].push_back(&wordList[i]);
            }
        }
        
        unordered_set<string*> visited;
        visited.insert(&beginWord);
        
        queue<pair<string, int>> bfs_queue;
        bfs_queue.push({beginWord, 1});
        
        while(!bfs_queue.empty()){
            string curr = bfs_queue.front().first;
            int steps = bfs_queue.front().second;
            bfs_queue.pop();
            
            for(int i=0;i<curr.size();i++){
                vector<string*>* neighbor = &graph[curr.substr(0,i) + "*" + curr.substr(i+1)];
                for(auto it=(*neighbor).begin(); it!=(*neighbor).end();it++){
                    if(**it==endWord) return steps+1;
                    if(visited.find(*it)==visited.end()){
                        visited.insert(*it);
                        bfs_queue.push({**it, steps+1});
                    }     
                }
            }   
        }
        return 0;
    }
};
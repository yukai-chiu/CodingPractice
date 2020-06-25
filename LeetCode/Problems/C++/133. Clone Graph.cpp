class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(!node) return NULL;
        
        //dfs traverse the graph and use visited to prevent cycle
        Node* root = new Node(node->val);
        queue<Node*> myqueue;
        myqueue.push(node);
        unordered_map<int, Node*> visited; 
        visited[1] = root;
        while(!myqueue.empty()){
            Node* cur = myqueue.front();
            myqueue.pop();
            for(auto n:cur->neighbors){
                if(visited.find(n->val)== visited.end()){
                    visited[n->val] = new Node(n->val);
                    visited[cur->val]->neighbors.push_back(visited[n->val]);
                    myqueue.push(n);
                    }
                else
                    visited[cur->val]->neighbors.push_back(visited[n->val]);   
                }
            }
        return visited[1];
    }
};
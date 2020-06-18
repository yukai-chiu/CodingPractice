class Solution {
public:
    int maxDepth(TreeNode* root) {
        //bfs
        if(!root) return 0;
        int depth = 0, max_depth = INT_MIN;
        queue<pair<TreeNode*,int>> myqueue;
        myqueue.push({root,0});
        TreeNode* curr;
        
        while(!myqueue.empty()){
            int level_size = myqueue.size();
            
            curr = myqueue.front().first;
            depth = myqueue.front().second;
            max_depth = max(max_depth, depth);
            myqueue.pop();
            if(curr){
                myqueue.push({curr->left,depth+1});
                myqueue.push({curr->right,depth+1});
            }
        }
        return max_depth;
    }
};
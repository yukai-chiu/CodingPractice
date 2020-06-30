//Time: O(n)
//Space: O(n)
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        
        queue<pair<TreeNode*, int>> myqueue;
        int min_depth = INT_MAX;
        myqueue.push({root, 1});
        
        while(!myqueue.empty()){
            TreeNode* curr = myqueue.front().first;
            int curr_depth = myqueue.front().second;
            myqueue.pop();
            //check if null
            if(!curr) continue;
            
            //if it's leaf
            if(!curr->left && !curr->right)
                min_depth = min(min_depth, curr_depth);
            
            myqueue.push({curr->left, curr_depth+1});
            myqueue.push({curr->right, curr_depth+1});
        }
        
        return min_depth;
    }
};
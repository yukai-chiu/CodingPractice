class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        queue<TreeNode*> myqueue;
        
        myqueue.push(root);
        
        while(!myqueue.empty()){
            vector<int> level;
            int size = myqueue.size();
            for(int i=0; i<size;++i){
                root = myqueue.front();
                myqueue.pop();
                if(root){
                    level.push_back(root->val);
                    myqueue.push(root->left);
                    myqueue.push(root->right);
                }
            }
            if(level.size() > 0){
                result.push_back(level);
            }
            
        }
        return result;
    }
};


class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root) return {};
        vector<vector<int>> result;
        queue<TreeNode*> myqueue;
        
        myqueue.push(root);
        
        while(!myqueue.empty()){
            vector<int> level;
            int size = myqueue.size();
            for(int i=0; i<size;++i){
                root = myqueue.front();
                myqueue.pop();
                level.push_back(root->val);
                if(root->left) myqueue.push(root->left);
                if(root->right) myqueue.push(root->right);    
            }       
            result.push_back(level);
        }
        return result;
    }
};
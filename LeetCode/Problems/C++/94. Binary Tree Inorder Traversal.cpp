//recursive
class Solution {
public:
    void inorder(TreeNode * node, vector<int>& result){
        if(!node){
            return;
        }
        inorder(node->left, result);
        result.push_back(node->val);
        inorder(node->right, result);
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        inorder(root, result);
        return result;
        
    }
};

//iterative
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> s;
        
        while(!s.empty()||root){
            //find the left most node
            while(root){
                s.push(root);
                root = root->left;
            }
            root = s.top();
            s.pop();
            result.push_back(root->val);
            root = root->right;
        }
        
        return result;
        
    }
};
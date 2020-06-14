//recursive
class Solution {
public:
    void preorder(TreeNode* node, vector<int>& result){
        if(node == NULL){
            return;
        }
        result.push_back(node->val);
        preorder(node->left, result);
        preorder(node->right, result);
        return;
    }
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        preorder(root, result);
        return result;
    }
};

//iterative
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> s;
        s.push(root);
        TreeNode* node = nullptr;
        while(!s.empty()){
            node = s.top();
            s.pop();
            if(!node){
                continue;
            }
            result.push_back(node->val);
            s.push(node->right);
            s.push(node->left);
        }
        return result;
    }
};
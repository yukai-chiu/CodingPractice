class Solution {
public:
    bool checkSymmetric(TreeNode* left, TreeNode* right){
        if(!left && !right) return true;
        if(!left || !right) return false;
        if(left->val != right->val) return false;
        
        return checkSymmetric(left->right, right->left) && checkSymmetric(right->right, left->left);
    }
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return checkSymmetric(root, root);
    }
};
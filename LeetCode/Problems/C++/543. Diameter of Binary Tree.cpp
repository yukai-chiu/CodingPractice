class Solution {
private:
    int dfs(TreeNode* root, int& diameter){
        if(!root) return 0;

        int l = dfs(root->left, diameter);
        int r = dfs(root->right, diameter);
        diameter = max(l+r, diameter);
        
        return max(l, r)+1;
    }
    
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if(!root) return 0;
        int diameter =INT_MIN;
        dfs(root, diameter);
        

        return diameter;
    }
};
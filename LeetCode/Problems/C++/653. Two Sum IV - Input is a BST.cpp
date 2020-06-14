/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
//dfs recursion
//Time: O(n)
//Space: O(n)
class Solution {
public:
    bool dfs(TreeNode* node, unordered_set<int>& lookup, int k){
        if(node == NULL) return false;
        if(lookup.count(k-node->val)){
            return true;
        } 
        
        lookup.insert(node->val);
        return dfs(node->left, lookup, k) || dfs(node->right, lookup, k);  
    }
    
    bool findTarget(TreeNode* root, int k) {
        unordered_set<int> lookup;
        
        return dfs(root, lookup, k);

    }
};
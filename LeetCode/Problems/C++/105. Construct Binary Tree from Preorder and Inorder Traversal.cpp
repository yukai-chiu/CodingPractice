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
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(!preorder.size() || !inorder.size()) return NULL;
        
        unordered_map<int, int> in_map;
        for(int i=0;i<inorder.size();i++){
            in_map[inorder[i]] = i;
        }
        
        stack<TreeNode*> mystack;
        TreeNode* head = new TreeNode(preorder[0]);
        mystack.push(head);
        
        for(int i=1;i<preorder.size();i++){
            TreeNode* node = new TreeNode(preorder[i]);
            if(in_map[preorder[i]] < in_map[mystack.top()->val])
                mystack.top()->left = node;
            else{
                TreeNode* parent;
                while(!mystack.empty() && in_map[mystack.top()->val] < in_map[preorder[i]]){
                    parent = mystack.top();
                    mystack.pop();
                }
                parent->right = node;
            }
            mystack.push(node);          
        }
        return head;
        
    }
};
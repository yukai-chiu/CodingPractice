/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        if(!root) return NULL;
        //case 1: p have right sub tree
        TreeNode* successor = NULL;
        TreeNode* node;
        if(p->right){
            node = p->right;
            while(node){
                successor = node;
                node = node->left;
            }
        }
        
        //case 2: search in BST
        else{
            node = root;
            while(node){
                //ending case: we want to make sure that we got the answer when reaching p
                if(node->val == p->val){
                    break;
                }
                else if(node->val < p->val){
                    node = node->right;
                }
                else if(node->val > p->val){
                    successor = node;
                    node = node->left;
                }
            }
        }
        return successor;

    }
    
};
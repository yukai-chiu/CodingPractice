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
class BSTIterator {
private:
    stack<TreeNode*> stack;
    TreeNode* head;
public:
    BSTIterator(TreeNode* root) {
        head = root;
        TreeNode* node = head;
        while(node!=NULL){
            stack.push(node);
            node = node->left;
        }
    }
    void checkRightSubTree(TreeNode* node) {
        if(node->right){
            stack.push(node->right);
            while(stack.top()->left != NULL)
                stack.push(stack.top()->left);
        } 
    }
    /** @return the next smallest number */
    int next() {
        TreeNode* curr = stack.top();
        stack.pop();
        checkRightSubTree(curr);
        return curr->val;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !stack.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
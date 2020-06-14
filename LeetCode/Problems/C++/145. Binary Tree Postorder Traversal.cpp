//hard iterative solution
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        if(!root){
            return {};
        }
        vector<int> result;
        stack<TreeNode*> s;
        TreeNode* last = nullptr;
        while(root || !s.empty()){
            if(root){
                s.push(root);
                root = root->left;
            }
            else{
                TreeNode* top = s.top();
                if(top->right && last != top->right){
                    root = top->right;
                }
                else{
                    result.push_back(top->val);
                    last = top;
                    s.pop();
                }   
            }  
        }
        return result;
    }
};



class Solution {
public:
    void postorder(TreeNode* root, vector<int>& result){
        if(!root) return;
        postorder(root->left, result);
        postorder(root->right, result);
        result.push_back(root->val);
        
    }
    vector<int> postorderTraversal(TreeNode* root) {
        if(!root){
            return {};
        }
        vector<int> result;
        postorder(root, result);
        return result;
    }
};


class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        if(!root){
            return {};
        }
        vector<int> result;
        stack<TreeNode*> s;
        s.push(root);
        while(!s.empty()){
            root = s.top();
            s.pop();     
            if(!root){
                continue;
            }
            result.insert(result.begin(),root->val);
            s.push(root->left);
            s.push(root->right);         
        }
        return result;
    }
};
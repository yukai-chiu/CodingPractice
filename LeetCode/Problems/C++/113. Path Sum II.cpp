//post order iterative
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> paths;
        vector<int> found_path;
        stack<TreeNode*> st;
        TreeNode* node = root;
        TreeNode* prev = NULL;
        while(node ||!st.empty()){
            if(node){
                st.push(node);
                found_path.push_back(node->val);
                sum -= node->val;
                node = node->left;  
            }
            else{
                node = st.top();
                if(node->right && prev != node->right){
                    //traverse right subtree
                    node = node->right;
                }
                else{
                    //leaf
                    if(!node->left && !node->right && sum ==0)
                        paths.emplace_back(found_path);
                    //backtracking
                    sum += node->val;
                    found_path.pop_back();
                    st.pop();
                    prev = node;
                    node = NULL;
                }
            }  
        }
        return paths;
    }
};


class Solution {
public:
    void findPath(TreeNode* node, vector<vector<int>>& paths, vector<int> path, int sum){
        if(node==NULL){
            return;
        }
        sum-= node->val;
        path.push_back(node->val);
        if(node->left == NULL && node->right == NULL && sum == 0){
            paths.push_back(path);
        }
        
        findPath(node->left, paths, path, sum);
        findPath(node->right, paths, path, sum);
    }
    
    
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> paths;
        
        findPath(root, paths, {}, sum);
        
        return paths;
    }
};
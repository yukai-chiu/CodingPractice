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



//recursive
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if(!root) return false;
        
        sum-=root->val;
        if(sum==0 && !root->left && !root->right){
            return true;
        }
        return hasPathSum(root->left, sum) || hasPathSum(root->right, sum);
    }
};


//iterative
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if(!root) return false;
        stack<pair<TreeNode*, int>> s;
        s.push({root,sum});
        
        while(!s.empty()){
            TreeNode* node = s.top().first;
            int curr_sum = s.top().second;
            s.pop();
            if(node==NULL){
                continue;
            }
            curr_sum-= node->val;
            
            if(node->left == NULL && node->right == NULL){
                if(curr_sum == 0) return true;
            }
            
            s.push({node->left, curr_sum});
            s.push({node->right, curr_sum});
            
        }
        
       return false;
    }
};
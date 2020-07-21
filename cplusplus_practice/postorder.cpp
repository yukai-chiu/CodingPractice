#include<stdlib.h>
#include<iostream>
#include<vector>
#include<queue>
#include<stack>
struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

std::vector<int> postorderTraversal(TreeNode* root) {
    if(!root) return {};
    std::vector<int> result;
    std::stack<TreeNode*> mystack;
    mystack.push(root);
    while(!mystack.empty()){
        TreeNode* curr = mystack.top();
        mystack.pop();
        if(!curr) continue;
        result.insert(result.begin(), curr->val);
        mystack.push(curr->left);
        mystack.push(curr->right);
    }
    return result;
    }
int main(){
    TreeNode* root = new TreeNode(1);
    std::priority_queue<int> q;
    postorderTraversal(root);


    return 0;
}
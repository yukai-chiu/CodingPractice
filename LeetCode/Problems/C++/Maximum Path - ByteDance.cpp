struct MyTreeNode {
    int val;
    MyTreeNode* left;
    MyTreeNode* right;
    MyTreeNode(int value){
        val = value;
        right = NULL;
        left = NULL;
    }
};
//Time complexity: O(n), n is the count of nodes, we traverse through all of the nodes in the tree once
//Space complexity: O(h), we are storing a path in the stack, so it will be O(h) where h is the height of the tree 
//average is O(logn) but worst case will be O(n) when the tree is skewed
vector<int> maxPathSum(MyTreeNode* root) {
        vector<int> path;
        vector<int> current_path;
        stack<MyTreeNode*> st;
        MyTreeNode* node = root;
        MyTreeNode* prev = NULL;
        int max_sum = 0;
        int current_sum = 0;
        
        while(node ||!st.empty()){
            if(node){
                st.push(node);
                current_path.push_back(node->val);
                current_sum += node->val;
                node = node->left;  
            }
            else{
                node = st.top();
                //traverse right subtree
                if(node->right && prev != node->right){
                    node = node->right;
                }
                else{
                    //if the current node is leaf
                    if(!node->left && !node->right && current_sum > max_sum){
                        max_sum = current_sum;
                        path = current_path;
                    }
                    //backtracking
                    current_sum -= node->val;
                    current_path.pop_back();
                    st.pop();
                    prev = node;
                    node = NULL;
                }
            }  
        }
        return path;
    }
int main() {
    

    //Construct testing tree
    //      5
    //    /  \
    //   4    8
    //  / \   / 
    // 11  7 13
    //
    MyTreeNode* root = new MyTreeNode(5);
    root->left = new MyTreeNode(4);
    root->right = new MyTreeNode(8);
    root->left->left = new MyTreeNode(11);
    root->left->right = new MyTreeNode(7);
    root->right->left = new MyTreeNode(13);

    vector<int> answer = maxPathSum(root);
    cout << "nodes of max path: ";
    for(auto i:answer){
        cout << i << " ";
    }
    
    return 0;
}
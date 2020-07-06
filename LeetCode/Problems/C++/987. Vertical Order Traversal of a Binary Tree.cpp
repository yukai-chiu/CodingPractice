//Time: O(nlog(n/k))
//Space: O(n)
class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        if(root == NULL) return {};
        vector<vector<int>> vertical_order;
        
        queue<pair<TreeNode*,pair<int,int>>> myqueue;
        
        myqueue.push({root, {0,0}});
        int min_col = INT_MAX;
        int max_col = INT_MIN;
        int level_size;
        
        unordered_map<int, vector<pair<int,int>>> column_table;
        while(!myqueue.empty()){
            level_size = myqueue.size();
            for(int i=0;i<level_size;i++){
                TreeNode* curr = myqueue.front().first;
                int col = myqueue.front().second.first;
                int row = myqueue.front().second.second;
                myqueue.pop();
                if(curr==NULL) continue;
                column_table[col].push_back({row, curr->val});
                max_col = max(max_col, col);
                min_col = min(min_col, col);
                myqueue.push({curr->left, {col-1, row+1}});
                myqueue.push({curr->right, {col+1, row+1}});
            }
        }
        
        for(int i=min_col;i<=max_col;i++){
            sort(column_table[i].begin(), column_table[i].end());
            vector<int> temp;
            for(int j=0;j<column_table[i].size();j++)
                temp.push_back(column_table[i][j].second);
            vertical_order.push_back(temp);
        }
        
        return vertical_order;
        
    }
};
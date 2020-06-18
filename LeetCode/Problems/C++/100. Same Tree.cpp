//recursive
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(!p && !q) return true;
        if((!p && q) || (!q && p)) return false;
        if(p->val != q->val) return false;
        
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        
    }
};

//iterative
class Solution {
public:
    bool checkSame(TreeNode* p, TreeNode* q){
        if(!p && !q) return true;
        if((!p && q) || (!q && p)) return false;
        if(p->val != q->val) return false;
        return true;
    }
    
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(!p && !q) return true;
        
        queue<pair<TreeNode*, TreeNode*>> myqueue;
        myqueue.push({p,q});
        
        while(!myqueue.empty()){
            p = myqueue.front().first;
            q = myqueue.front().second;
            myqueue.pop();
            
            if(checkSame(p,q)){
                if(p){
                    myqueue.push({p->left, q->left});
                    myqueue.push({p->right, q->right});
                }
            }
            else return false;
        }
        return true;  
    }
};
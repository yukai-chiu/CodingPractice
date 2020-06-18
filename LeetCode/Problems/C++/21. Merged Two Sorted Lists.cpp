class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(!l1 && !l2) return NULL;
        
        ListNode* root = new ListNode();
        ListNode* curr = root;
        
        while(l1 && l2){
            if(l1->val <= l2->val) {
                curr->next = new ListNode(l1->val); 
                l1 = l1->next;          
            }
            else{
                curr->next = new ListNode(l2->val); 
                l2 = l2->next;
            }
            curr = curr->next;
        }
        while(l1){
            curr->next = new ListNode(l1->val); 
            l1 = l1->next;    
            curr = curr->next;
        }
        while(l2){
            curr->next = new ListNode(l2->val); 
            l2 = l2->next;    
            curr = curr->next;
        }
        return root->next;
    }
};
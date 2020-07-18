/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==NULL) return NULL;
        
        ListNode* prev = new ListNode(-1);
        prev->next = head;
        ListNode* root = prev;
        ListNode* curr = head;
        
        while(curr){
            
            if(curr->next && curr->val == curr->next->val){
                int val = curr->val;
                while(curr && curr->val == val)
                    curr = curr->next; 
                prev->next = curr;
            }
            else{
                prev = prev->next;
                curr = curr->next;
            }     
        }
        return root->next;
    }
};
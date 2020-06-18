//Time: O(n)
//Space: O(1)
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head || !head->next)
            return head;
        
        ListNode* curr = head;
        ListNode* prev = NULL;
        while(curr){
            ListNode* temp = curr->next;
            curr->next = prev;
            
            prev = curr;
            curr = temp;
        }
        return prev;
    }
};
//Time: O(n)
//Space: O(n)
class Solution {
public:
    
    ListNode* reverseList(ListNode* head) {
        if(!head || !head->next)
            return head;
        
        ListNode* node = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return node;
    }
};
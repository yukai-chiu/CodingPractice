/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL) return false;
        
        ListNode* fast = head;
        ListNode* slow = head;
        int step = 0;
        while(fast){
            if(step%2==1) slow = slow->next;
                  
            fast = fast->next;     
            if(fast==slow) return true;
            step++;
        }
        return false;
    }
};
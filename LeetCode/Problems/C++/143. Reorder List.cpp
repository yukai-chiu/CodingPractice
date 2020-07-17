//Time: O(n)
//Space: O(1)
class Solution {
public:
    void reorderList(ListNode* head) {
        if(head == NULL) return;
        
        //step 1: find the mid point
        ListNode* fast = head->next;
        ListNode* slow = head;
        
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        //slow will be the node before the second part
        
        //step 2: reverse the second part
        ListNode* prev = NULL;
        ListNode* curr = slow->next;
        //break the link
        slow->next = NULL;
        
        while(curr){
            ListNode* temp = curr->next;
            curr->next = prev;
            //take a step
            prev = curr;
            curr = temp;   
        }
        
        ListNode* node1 = head;
        ListNode* node2 = prev;
        //step 3: merge two list
        while(node1 && node2){
            ListNode* temp1 = node1->next; 
          
            
            node1->next = node2;
            //take a step
            node2 = node2->next;
            node1->next->next = temp1;
            node1 = temp1;

        }

    }
};
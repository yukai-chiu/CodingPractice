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
    
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        node = head;
        size = 0;
        while(node!= NULL){
            size++;
            node = node->next;
        }
        node = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        ListNode* rand_node = node;
        int index = rand() % size;
        while(index>0){
            rand_node = rand_node->next;
            index--;
        }
        return rand_node->val;
        
    }
private:
    ListNode* node;
    int size;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
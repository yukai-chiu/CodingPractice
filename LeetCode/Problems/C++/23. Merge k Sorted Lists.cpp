class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(!lists.size()) return NULL;
        
        ListNode* head = new ListNode();
        ListNode* node = head;
        priority_queue<pair<int, ListNode*>> merge_q;
        for(int i=0;i<lists.size();i++)
            if(lists[i])
                merge_q.push({-lists[i]->val,lists[i]});
        
        while(!merge_q.empty()){
            ListNode* curr = merge_q.top().second;
            merge_q.pop();
            node->next = curr;
            node = node->next;
            if(curr->next)
                merge_q.push({-curr->next->val, curr->next});
        }
        
        
        return head->next;
    }
};
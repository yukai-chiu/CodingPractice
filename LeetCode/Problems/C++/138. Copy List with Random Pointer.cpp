/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head == NULL) 
            return NULL;
        
        unordered_map<Node*, Node*> visited;
        Node* root = new Node(head->val);
        Node* curr = root;
        visited[head] = root;
        while(head!= NULL){
            Node* temp_next;
            if(head->next!= NULL){
                if(visited.find(head->next) == visited.end()){
                    temp_next = new Node(head->next->val);
                    visited[head->next] = temp_next;
                }
                else
                    temp_next = visited[head->next];
            curr->next = temp_next;
            }
            
                 
            Node* temp_random;
            if(head->random!= NULL){
                if(visited.find(head->random) == visited.end()){
                    temp_random = new Node(head->random->val);    
                    visited[head->random] = temp_random;
 
                }
                else{
                    temp_random = visited[head->random];
                }
            curr->random = temp_random;
            }   
            curr = curr->next;
            head = head->next;  
        }
        
        return root;
    }
};
struct LinkedNode{
    int val;
    LinkedNode* next;
    LinkedNode(int x){
        val = x;
        next = NULL;
    }
};

class MyLinkedList {
private:
        LinkedNode* head;
        int size;
public:
    /** Initialize your data structure here. */
    MyLinkedList() {
        head = new LinkedNode(0);
        size = 0;

    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if(index>=size) return -1;
        
        LinkedNode* curr = head->next;
        int i = 0;
        while(i<index){
            curr = curr->next;
            ++i;
        }
        return curr->val;
    }
    
   
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        LinkedNode* temp = head->next;
        head->next = new LinkedNode(val);
        head->next->next = temp; 
        size++;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
    
        LinkedNode* prev = head;
        while(prev->next){
            prev = prev->next;
        }   
        LinkedNode* curr = new LinkedNode(val);
        prev->next = curr;  
        size++;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if(index > size) return;
        LinkedNode* prev = head;
        int i = 0;
        while(i<index){
            prev = prev->next;
            i++;
        }
           
        LinkedNode* curr = new LinkedNode(val);
        curr->next = prev->next;
        prev->next = curr;
        size++;
        
 
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if(index >= size) return;
        
        LinkedNode* curr = head;
        int i = 0;
        while(i<index){
            curr = curr->next; 
            i++;
        }
        curr->next = curr->next->next;
        size--;
    }

};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
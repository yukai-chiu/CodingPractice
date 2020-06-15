class DLinkedNode:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        #hashmap + double linked list
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev= self.head


    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        #move the accessed node to head
        self._move_to_head(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        
        node = self.cache.get(key)
        
        if not node:
            #add 
            node = DLinkedNode()
            node.val = value
            node.key = key
            self.cache[key] = node
            self._add_node(node)  
            self.size+=1
            
            #check if over capacity
            if self.size > self.capacity:
                to_remove = self._pop_tail()
                del self.cache[to_remove.key]
                self.size-=1
            
            
        else:
            #update the val
            node.val = value
            self._move_to_head(node)
            
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
        
        
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _pop_tail(self):
        last = self.tail.prev
        self._remove_node(last)
        return last


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
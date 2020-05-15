########################################
####Trie
########################################
class TrieNode:
    def __init__(self):
        self.child = {}
        self.score = 0
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key,0)
        self.map[key] = val
        curr = self.root
        for c in key:
            curr = curr.child.setdefault(c, TrieNode())
            curr.score += delta
        
        

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.child:
                return 0
            curr = curr.child[c]
        return curr.score
            


########################################
####Hashmap
########################################
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.score = {}#collections.Counter()
        

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key,0)
        self.map[key] = val
        
        for i in range(len(key)):
            score = self.score.setdefault(key[:i+1],0)
            self.score[key[:i+1]] += delta
            
        
        

    def sum(self, prefix: str) -> int:
     
        return self.score[prefix] if prefix in self.score else 0
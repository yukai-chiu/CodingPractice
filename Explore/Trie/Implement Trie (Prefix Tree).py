class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.data = None
        self.word = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self
        for c in word:
            if c not in curr.child:
                curr.child[c] = Trie()
                curr.child[c].data = c
            curr = curr.child[c]
        curr.word = True
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self
        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self
        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
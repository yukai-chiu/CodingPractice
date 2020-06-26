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


class TrieNode:
    def __init__(self):
        self.val = ""
        self.child = {}
        self.end = None
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
                
            curr = curr.child[ch]
        curr.end = word
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                return False
            else:
                curr = curr.child[ch]
        if curr.end == word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for ch in prefix:
            if ch not in curr.child:
                return False
            else:
                curr = curr.child[ch]
                
        queue = [curr]
        while queue:
            curr = queue.pop(0)

            if curr.end != None:
                return True
            for key in curr.child:
                queue.append(curr.child[key])
                
        
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
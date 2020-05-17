class TrieNode(object):
    def __init__(self):       
        self.child = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for c in word:
            curr = curr.child.setdefault(c,TrieNode())
        curr.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        stack = [(self.root,word)]

        while stack:
            curr, curr_word = stack.pop()

            if not curr_word:
                if curr.isEnd:
                    return True
            
            elif curr_word[0] == ".":
                for child in curr.child:
                    stack.append((curr.child[child],curr_word[1:]))
            elif curr_word[0] in curr.child:
                stack.append((curr.child[curr_word[0]],curr_word[1:]))
        return False
            

        
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
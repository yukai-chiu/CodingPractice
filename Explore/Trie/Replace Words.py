class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.isEnd = False
        self.word = None

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        if not sentence or sentence == "":
            return ""
        
        #create Trie
        root = TrieNode()
        
        #construct Trie
        for i,r in enumerate(dict):
            curr = root
            for c in r:
                curr = curr.child.setdefault(c,TrieNode())
                
            curr.isEnd = True
            curr.word = r
            
        result = sentence.split(" ")
        for i, word in enumerate(result):
            curr = root
            for c in word:
                if c in curr.child:
                    curr = curr.child[c]
                    if curr.isEnd:
                        result[i] = curr.word   
                        break
                else:
                    if curr.isEnd:
                        result[i] = curr.word     
                    break
        return " ".join(result)
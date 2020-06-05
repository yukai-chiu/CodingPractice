class TrieNode:
    def __init__(self):
        self.child = {}
        self.id = -1
        self.remain_palindrome = []
        
        
    def addWord(self, word, i):
        
        curr = self
        for j, c in enumerate(reversed(word)):

            if isPalindrome(word[0:len(word)-j]):
                curr.remain_palindrome.append(i)

            curr = curr.child.setdefault(c,TrieNode())
        curr.id = i
        
def isPalindrome(word):
    #if len(word) == 0 or len(word) == 1:
    #    return True
    for i in range(len(word)//2):
        if word[i] != word[-1 - i]:
            return False
    return True
        
class Solution:
    
    
    
    def getPalindromeFromWord(self, curr, word, index):
        
        result = []
        for j, c in enumerate(word):
            #case 1: 
            #if word in trie is shorter, meet the end in the trie first
            #check if the remaining of the currert word_j is palindrome
            if curr.id >=0 and index != curr.id:
                print(word, word[j:],isPalindrome(word[j:]))
                if isPalindrome(word[j:]):
                    result.append([index,curr.id])

            if c not in curr.child:
                
                return result
            curr = curr.child[word[j]]
           
            
        #if both have the same length
        if curr.id>=0  and index != curr.id:
            result.append([index,curr.id])
        #if word in trie is longer
        #can form more palindrome

        for k in curr.remain_palindrome:
            if index != k:
                result.append([index,k])
        return result
    
            
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        if not words:
            return []
        
        result = []
        #construct trie
        self.root = TrieNode()
        for i, word in enumerate(words):
            self.root.addWord(word,i)#constructTrie(words)
        
        
                
        #traverse
        
        for i, word in enumerate(words):
            curr = self.root
            result.extend(self.getPalindromeFromWord(curr, word,i))
            
              
        return result
                
            
                
                
        
        
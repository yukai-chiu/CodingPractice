class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if not words:
            return 0
        lookup = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        count = set()
        
        for w in words:
            transform = ""
            for ch in w:
                transform+=lookup[ord(ch) -ord('a')]
            count.add(transform)
            
        return len(count)
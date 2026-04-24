class TrieNode:
    
    def __init__(self, c):
        self.val = c
        self.children = {} # { character -> TrieNode } 
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode(".")
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c] # keep traversing until you get to the last character
        return cur.endOfWord

        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c] # keep traversing until you get to the last character
        return True 

        
        
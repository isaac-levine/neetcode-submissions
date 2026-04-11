class TrieNode:
    def __init__(self):
        self.endOfWord = False 
        self.children = {} # char -> TrieNode

class PrefixTree:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            # create the node if it doesn't exist. 
            if c not in node.children: 
                node.children[c] = TrieNode()

            # move pointer to the child node
            node = node.children[c] 
        node.endOfWord = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            else:
                node = node.children[c]

        return node.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        return True 
        
        
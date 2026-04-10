class Node:
    def __init__(self):
        self.children = {} # c -> Node
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    # add the given word to the prefix tree
    # remember to mark last character as end_of_word
    def insert(self, word: str) -> None:
        if len(word) == 0:
            return

        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node() # add the node for this character if it doesn't exist 
            cur = cur.children[c] # move cur to the node for this character
        
        cur.end_of_word = True

    # does the prefix tree contain the given word?
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        
        return cur.end_of_word # if we make it through all letters, only thing to check is whether last letter is an ender

        
    # is there some word that has the given prefix?
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        
        return True

        
        
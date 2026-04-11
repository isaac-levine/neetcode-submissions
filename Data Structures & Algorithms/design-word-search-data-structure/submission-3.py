class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() 

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode() 
            node = node.children[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(j, cur):
            for i in range(j, len(word)):
                c = word[i]
                
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                        
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        
        return dfs(0, self.root)


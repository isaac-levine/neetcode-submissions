class TrieNode:
    def __init__(self, c):
        self.val = c
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode(None)
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word: 
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(i, cur):
            if i == len(word):
                return cur.endOfWord
            elif word[i] == ".":
                for c in cur.children:
                    if dfs(i + 1, cur.children[c]):
                        return True
                return False
            elif word[i] in cur.children:
                return dfs(i + 1, cur.children[word[i]])
            return False


        return dfs(0, self.root)

class TrieNode:
    def __init__(self):
        self.children = {} # character -> TrieNode
        self.endOfWord = False
        self.wordsIndex = -1 

    # Add a word to the Trie
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # 1. Create a Trie with all the words 
        # The Trie helps us "prune the search space" early. -- meaning we stop exploring paths that can't 
        # possibly lead to a valid word before we waste any more time on them. 
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0]) 
        res = set() # resulting words, will be converted to list at the end. this is to avoid duplicate resulting words. 

        # this is our path tracking set. 
        visit = set() # used by each DFS path. gets cleared/reset when you backtrack "path tracking"
 
        # starting from position (r,c), add the word to our result set if we can make it to the end of a word 
        # During DFS, we're going to follow any and all paths that match/respect the Trie structure. 
        # And when we reach an endOfWord, add it to the result set. 
        def dfs(r, c, node, curWord):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c)) # mark this as visited for the rest of this recursive path. 

            node = node.children[board[r][c]]
            curWord += board[r][c]
            if node.endOfWord:
                res.add(curWord)

            dfs(r + 1, c, node, curWord)
            dfs(r - 1, c, node, curWord)
            dfs(r, c + 1, node, curWord)
            dfs(r, c - 1, node, curWord)
            visit.remove((r, c)) # undo the work (backtacking)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)
        
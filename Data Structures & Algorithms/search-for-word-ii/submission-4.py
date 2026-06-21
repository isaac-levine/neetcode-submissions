class TrieNode:
    def __init__(self, c):
        self.val = c
        self.children = {} # need to remember that this is a hashmap not a list
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        

        # build a Trie from the given list of words 
        # O(n) time and space where n is the total number of characters in all the words
        root = TrieNode(None)
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode(c)
                cur = cur.children[c]
            cur.endOfWord = True

        

        res = set() # list of words that we found 
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, node, curWord):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or board[r][c] not in node.children:
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            curWord += board[r][c]
            if node.endOfWord:
                res.add(curWord)
            
            dfs(r + 1, c, node, curWord)
            dfs(r - 1, c, node, curWord)
            dfs(r, c + 1, node, curWord)
            dfs(r, c - 1, node, curWord)
            visit.remove((r, c)) # backtracking -- need to study this 

        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
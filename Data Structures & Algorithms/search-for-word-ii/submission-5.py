class TrieNode:
    def __init__(self, c):
        self.children = {} # c -> TrieNode(c)
        self.c = c
        self.endOfWord = False 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        head = TrieNode(None)
        # build a trie from the words so that we can more efficiently check if our current
        # path is building a valid word in

        # bat, back 
        for w in words:
            cur = head
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode(c)
                cur = cur.children[c]
            cur.endOfWord = True

        completed_words = set()
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r, c, cur_word, trie, path):
            # success base case: reached the end of some word 
            if trie.endOfWord:
                completed_words.add(cur_word)
            # fail base case: out of bounds, in path (cycle), or bad letter
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in path or board[r][c] not in trie.children:
                return
            
            # add this letter to cur_word, and move trie pointer
            path.add((r, c)) # can't reuse this letter
            cur_word += board[r][c]
            trie = trie.children[board[r][c]]

            # try moving in all 4 directions 
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, cur_word, trie, path)
            path.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in head.children:
                    dfs(r, c, "", head, set()) # go find the word, same cell may not be used in more than one owrd

        return list(completed_words)

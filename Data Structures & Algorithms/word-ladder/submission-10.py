class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # off bat I think we need the beginword and endword to be the dimensions of a 2d dp array
        # or is it just a dfs?
        # actually yeah I think it's more of a graph problem than a DP problem tbh
        # the graph represents states and you can traverse to nearby words 
        # ugh I remember the adj list building for this one being a bit of a pain 
        # minimum number of transformations = shortest path = BFS?

        adj = defaultdict(list) # pattern -> [word1, word2, ...]
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        q = deque() 
        q.append(beginWord)
        numWords = 0
        visit = set() 
        while q:
            numWords += 1

            for _ in range(len(q)):
                word = q.popleft()
                if word in visit:
                    continue 
                elif word == endWord:
                    return numWords
                
                visit.add(word)
                
                # check each possible pattern to get neighbors from adj 
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            q.append(nei)

        
        return 0
        

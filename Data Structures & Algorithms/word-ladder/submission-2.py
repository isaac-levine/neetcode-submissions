class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # shortest path unweighted -> BFS
        if endWord not in wordList:
            return 0
        
        # build "adjacency list" of every possible "pattern" (e.g. "*at") to applicable words (e.g. "cat")
        # it's not technically an adjacency list because its patterns -> List(words) instead of word -> List(words)
        buckets = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                buckets[word[:i] + "*" + word[i + 1:]].append(word)

        
        q = deque() 
        q.append(beginWord)
        visit = set([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft() 
                visit.add(word)
                
                if word == endWord:
                    return res

                # get all the other words for all patterns for this current word (gives us the full set of "neighbors")
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neighbor in buckets[pattern]:
                        if neighbor not in visit:
                            q.append(neighbor)



            res += 1


        return 0


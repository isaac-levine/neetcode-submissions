class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        # patterns -> words
        # return minimum number of words within the transformation sequence. 

        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord) # ?

        # create a map of all types of patterns to all words
        patternMap = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                patternMap[pattern].append(word)

        # instead of a normal adjancency list graph representation, we have the pattern map 
        # we know word length is small and word list is also small...
        # so do we need to loop through all patterns on every iteration to find neighbors? 

        # shortest path from beginWord to endWord --> BFS? 
        q = deque()
        q.append(beginWord)
        visited = set()
        res = 1 
        while q:
            for _ in range(len(q)):
                word = q.popleft() 
                if word == endWord:
                    return res
                visited.add(word)
                

                # find all patterns for this word and queue up words corresponding to those patterns for the next layer of BFS 
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighborWord in patternMap[pattern]:
                        if neighborWord not in visited:
                            q.append(neighborWord)

            res += 1 # we care about the number of BFS layers

        return 0

        

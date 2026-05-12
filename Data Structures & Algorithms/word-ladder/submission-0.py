class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0 

        # 1. build our adjacency list         
        adjList = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adjList[pattern].append(word)

        # 2. BFS. if we find the word, return result
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                # get all the patterns, and then all the neighbors for each pattern. 
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighbor in adjList[pattern]:
                        if neighbor not in visit: 
                            visit.add(neighbor)
                            q.append(neighbor)

            
            res += 1 # increment result after we go through the entire layer


        return 0 
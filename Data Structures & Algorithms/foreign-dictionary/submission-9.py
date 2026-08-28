class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # return a valid topological ordering of the letters (alphabet)
        # so this is topological sort actually...
        # iirc topological sort you walk all neighbors, append, then unwind? 
        # feel like there's a name for this algorithm other than top sort but not sure 

        # plan:
        # 1. loop through our words, comparing words to find out nodes and edges,
        # where an edge a --> b means a must come before b
        # make sure each letter gets a corresponding node representation ?
        # this step 1 can be brute force through the words/characters because words are small and 
        # wordList is also small 

        # 2. dfs function with path set, (if we hit a cycle return "")
        # explore all neighboring nodes, then append to res

        # 3. call dfs from every letter node

        # remember might need to return the reverse of the result

        adj = {c : set() for word in words for c in word}
        for i in range(len(words) - 1): # i is the words list pointer
            w1, w2 = words[i], words[i + 1]
            smallerLen = min(len(w1), len(w2))
            # check for case where word2 is smaller and a prefix of word1, means there is no possible solution....
            if len(w1) > len(w2) and w2 == w1[:len(w2)]:
                return ""
            # find first differing character
            for j in range(smallerLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                
                

        # now that we have the graph built, we just need to get the topological ordering and make sure there are no cycles

        res = [] # list of characters 
        visited = set()
        def dfs(c, path):
            if c in path: return False
            if c in visited: return True
            
            path.add(c)
            for nei in adj[c]:
                if not dfs(nei, path):
                    return False
            
            path.remove(c)
            visited.add(c)
            res.append(c)
            return True


        for c in adj: 
            if not dfs(c, set()):
                return "" 

        return "".join(res[::-1])
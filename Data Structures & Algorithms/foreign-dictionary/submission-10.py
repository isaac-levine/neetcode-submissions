class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # off bat i remember this is a topological sort problem 
        # we can use first differing letter between every two adjacent words in the list
        # to find edges between different letters. 

        # then we have a graph...and then we can get topSort by doing dfs()...explore neighbors, then append, then reverse result? 

        adj = defaultdict(list) # {a : [b, c]}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # traverse letters in w1 because either w1 is smaller, or there is a differing character
            for j in range(min(len(w1), len(w2))):
                if len(w2) < len(w1) and w2 == w1[:len(w2)]:
                    return ""
                if w1[j] != w2[j]:
                    # we know w1[j] > w2[j] lexicographically 
                    adj[w1[j]].append(w2[j])
                    break

        # do we need a visit set for top sort? I think so 
        # yeah because we need cycle detection to see if there's a valid lexicographical order
        visit = set() 
        path = set() 
        topSort = [] 
        def dfs(c):
            if c in path: return False
            if c in visit: return True 
            
            path.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            topSort.append(c)
            visit.add(c)
            path.remove(c)
            
            return True

        for word in words:
            for c in word:
                if not dfs(c):
                    return ""
        return "".join(topSort[::-1])
        
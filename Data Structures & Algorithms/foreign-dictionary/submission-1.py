class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {c : set() for w in words for c in w} # set to make sure we don't have duplicates
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) # we know character in word 2 comes after character in word 1
                    break
        
        # dfs
        visit = {} # false means character has not been visited, true means in current path, not in dict at all means not visited at all
        res = [] # we will join the characters in reverse order at the end. 
        def dfs(c):
            if c in visit:
                return visit[c] # t/f -- true means we saw it twice. false means we haven't seen it in this path.
            
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            visit[c] = False # no longer in current path
            res.append(c) # now, can finally append this character -- building this in reverse order

        
        for c in adj:
            if dfs(c):
                return "" # detected a loop
            
        res.reverse() 
        return "".join(res)
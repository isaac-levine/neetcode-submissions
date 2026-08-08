class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
    
        # if there is no topological order, return "" --> does that mean cycle? 
        # each word is essentially a disconnected component directed graph 
        # h -> r -> n
        # h comes before r comes before n

        adj = {c : set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # if they have the exat same prefix, but first word is longer, then this is an invalid ordering in the input
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            # find the first differing character
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # character in w1 comes before the character in w2 
                    adj[w1[j]].add(w2[j])
                    break
                

        res = [] 
        # visited = set()
        # Neetcode does visit = {} with False=visited and True=in current path
        visit = {}

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True # add to path

            for nei in adj[c]:
                if dfs(nei):
                    return True # if any neighbors find a loop, we must return True.
            
            # post-order: after processing neighbors, we can add this node to result
            visit[c] = False # remove from path
            res.append(c)
            

        for c in adj:
            if dfs(c):
                return "" # if we detect a loop

        res.reverse()
        return "".join(res)


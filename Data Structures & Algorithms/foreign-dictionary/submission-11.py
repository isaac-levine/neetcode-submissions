class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # off bat I remember that this is a graph problem. 
        # order unknown -> topological sort? 
        # words are sorted lexicogpraphically
        # if there is on valid lexicographical order...return ""

        # return string of letters in lexicogrpahically increasing order 

        # i remember from last time that we take every 2 adjacent words and iterate over min 

        adj = defaultdict(list) # c -> [c, c] where those neighbors are lexicographically bigger

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            # prefix invalid case. longer word is first and second word is a prefix
            if len(word1) > len(word2) and word2 == word1[:len(word2)]:
                return ""

            # normal case, first differing character
            for j in range(min(len(word1), len(word2))):
                c1, c2 = word1[j], word2[j]
                if c1 != c2:
                    # c1 is lexicographically smaller than c2.
                    adj[c1].append(c2)
                    break
        
        # then for topological sort you dfs exploring all neighbors then append yourself. 
        # so basically you explore all the way to lexicographically biggest leaf then append
        # so you need to reverse the result 
        res = []
        path, visit = set(), set() 
        def dfs(c):
            if c in path:
                return False
            if c in visit:
                return True
            path.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            res.append(c)
            path.remove(c)
            visit.add(c)
            return True 

        for w in words:
            for c in w:
                if not dfs(c):
                    return ""
        
        return "".join(res[::-1])
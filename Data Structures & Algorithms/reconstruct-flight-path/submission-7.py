class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # claude spoiled to me that this is hierholzer's. and I remember from the bus sheet that hierholzer's is 
        # an algorithm for finding an eulerian path. i.e. a path that uses every (directed?) edge exactly once? (can revisit nodes)

        # tickets are edges of course, reconstruct the path from JFK to wherever.  each edge useed exactly once 
        # return the lexicographically smallest one -- I think we just have to order our adj list accordingly to handle this 

        # not sure if im remembering correctly, but I think for this algorithm we just pop off from the adj list? 

        # adj list with {src -> destA, destB} where A, B are in lex. order 
        # so do you just order the tickets by destination and process in that order then? 

        # A: C, B
        # B: A
        # C: A 

        # A, B, A, C, A

        # [B,A], [C,A], [A,B], [A,C]

        res = []
        adj = defaultdict(deque) 

        tickets.sort() # sort tickets by lex. smallest destination 
        # feel like its supposed to just be a normal sort. i guess it doesn't matter 
        # for building the adj list because ties with t[0] it'll go to t[1] anyways so the list part of the adj list
        # will still be in sorted order...

        for src, dest in tickets:
            adj[src].append(dest)

        def dfs(node):
            # don't need to check visit or anything like that since we're popping nodes (won't reuse edge)
            # and we're allowed to revisit 
            while adj[node]: # you will literally just abandon edges if you make this an 'if' instead of a 'while'
                dfs(adj[node].popleft()) # pop and visit the last node 
            
            res.append(node)
        
        dfs("JFK")
        return res[::-1]



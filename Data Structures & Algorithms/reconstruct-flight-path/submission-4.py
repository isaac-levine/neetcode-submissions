class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        

        # MST algorithms
        # prim's
        # the union find one... Bellman-Ford? 

        # wrong. it's not an MST problem. You don't need to visit every node. You just need to get from src to dest....

        # eulerian path....wtf even is that

        # hierholzer's algorithm for finding an eulerian path in a graph...
        # walk until stuck, append, unwind (implicit return in this case)

        # we know there is at least one valid path.

        adj = defaultdict(deque)
        for src, dest in sorted(tickets):
            adj[src].append(dest)
        
        res = [] # builds in reverse order because we walk all the way to the end first.

        def dfs(node):

            while adj[node]:
                # why are we popping and modifying the neighbors instead of jsut looping through?
                # is this to kind of avoid having to use a visited set? 
                neighbor = adj[node].popleft()
                dfs(neighbor)

            res.append(node)

        dfs("JFK")
        return res[::-1]

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t)) # source : (dest, cost)

        res = 0 # the maximum cost will be the result 
        minHeap = [(0, k)] # dijkstra's starts with a source node, unlike Prim's 
        visited = set() 

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            res = cost # new maximum cost is res because we know we're going in increasing cost order 
            
            for neiNode, neiCost in adj[node]:
                if neiNode not in visited:
                    heapq.heappush(minHeap, (cost + neiCost, neiNode))

        
        return res if len(visited) == n else -1


        

        
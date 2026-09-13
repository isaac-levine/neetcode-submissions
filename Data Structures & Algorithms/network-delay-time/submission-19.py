class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # minimum time it takes for all n nodes to receive a signal = MST

        # i know there's the basic MST algorithm (is it Prim's, yeah i think thats prims) where we just do dijkstra's but with edge cost instead of total cost

        # since we have all the edges right away, why not just do that? 

        # so it's a greedy bfs where we have a maxHeap of edges to process 

        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        # 1 -> 4, 2
        # 2 -> 3
        # 4 -> 
        # 3 -> 4

        minHeap = []  # (4,4) (2,1)
        minHeap.append((0, k)) # (-cost, node)
        time = 0  # 0
        visit = set()

        while minHeap:
            cost, node = heapq.heappop(minHeap) # wait but will this break our while condition right away....no I think it'll reevaluate it after
            if node in visit: continue 
            time = cost
            visit.add(node)
            
            for nei, neiCost in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, ((cost + neiCost), nei)) # just this edge cost, not cost of total path.


        return time if len(visit) == n else -1 





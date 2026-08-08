class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v)) # (weight, dest)

        t = 0
        visited = set()
        minHeap = [(0, k)]

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue

            visited.add(node)
            t = cost # this only ever goes up

            for neiCost, neiNode in adj[node]:
                if neiNode not in visited:
                    heapq.heappush(minHeap, (neiCost + cost, neiNode))
            
            
        
        return t if len(visited) == n else -1
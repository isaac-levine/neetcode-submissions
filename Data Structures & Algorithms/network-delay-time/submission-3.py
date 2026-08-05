class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # k is the source node 
        
        adjList = defaultdict(list) 
        for u, v, w in times:
            adjList[u].append((v, w)) # source : (neighbor, weight)

        minHeap = [(0, k)] # (cost, node)

        # the shortest path from k to each other node i
        shortest = {} 

        while minHeap:
            cost, node = heapq.heappop(minHeap) 
            if node in shortest:
                continue
            shortest[node] = cost

            for nei, neiCost in adjList[node]:
                if nei not in shortest:
                    heapq.heappush(minHeap, ((neiCost + cost), nei))

        return max(shortest.values()) if len(shortest) == n else -1 
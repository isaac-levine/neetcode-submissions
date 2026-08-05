class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = defaultdict(list) 
        for u, v, w in times:
            adjList[u].append((v, w)) # source : (neighbor, weight)

        minHeap = [(0, k)] # (cost, node)
        visit = set()
        res = 0

        while minHeap:
            cost, node = heapq.heappop(minHeap) 
            if node in visit:
                continue
            visit.add(node)
            res = cost # every pop from the heap has cost >= the last one

            for nei, neiCost in adjList[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, ((neiCost + cost), nei))

        return res if len(visit) == n else -1 
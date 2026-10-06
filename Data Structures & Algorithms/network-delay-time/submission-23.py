class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # given a weighted directed graph 
        # and a source node 
        # return minimum time for all nodes to receive the signal 
        # i.e. shortest path that covers all nodes 

        # its not MST because it does actually matter where we start, so it must be Dijkstra's 
        # it's just Dijkstra's but instead of a destination node, we are done when all nodes are visited. 

        # remember dijkstra's is a greedy BFS with a minHeap of total path cost 
        # i think maybe kahn's is a more natural fit if you're given edges but i dont remember that 
        # one or know if I ever even learned it tbh

        # 1. build adj list
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        minHeap = [(0, k)] # 0 cost for source k
        visit = set() 

        while minHeap and len(visit) < n:
            time, node = heapq.heappop(minHeap)
            if node in visit:
                continue 
            visit.add(node)

            if len(visit) == n:
                return time 

            for nei, neiTime in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (time + neiTime, nei))

        return -1 
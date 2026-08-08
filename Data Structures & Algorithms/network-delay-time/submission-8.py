class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # minimum time it takes for all of the nodes to receive the signal 

        # k is the source node 

        # dijkstra's from source node k
        # then just validate that we've visited every node len(visted) == n 
        # result will be number of iterations / layers of the BFS.


        # build an adjacency list
        adj = {i: set() for i in range(1, n + 1)}
        for s, d, t in times:
            adj[s].add((t, d)) # s : (edgeCost, dest)

        # 1: (1,2), (4,4)
        # 2: (1,3)
        # 3: (1,4)
        # 4: 

        # minHeap = [ (1,2), (4,1) ]

        # res = 1
        visited = set()
        minHeap = [(0, k)] # (totalCost, dest)
        res = 0
        # visited = set() -- do we need a visited set for dijkstra's?

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue

            for neiTime, neiNode in adj[node]:
                if neiNode not in visited:
                    heapq.heappush(minHeap, (time + neiTime, neiNode)) # push (totalTime, neighborNode) to heap


            res = time
            visited.add(node)


        return res if len(visited) == n else -1 
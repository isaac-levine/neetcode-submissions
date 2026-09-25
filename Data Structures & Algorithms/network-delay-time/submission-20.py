class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # weighted edges (times)
        # off bat i remember this problem being the canonical problem for something either dijkstra's or prims or something like that 

        # oh i remember this. and i even remember the mistake I made before, I thought it was an MST problem but its really just dijkstra's. 
        # because we are minimizing the time from the source node 
        # not the total time of the tree if that makes sense...i think thats the correct distinction???

        # 1. build simple adj list with edge weights 
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        print(adj)
        
        # dijkstra's is a greedy bfs where you traverse the cheapest available total edge path cost 
        minHeap = [(0, k)] # the signal starts from k -- and there is of course 0 cost for us to get there because thats where the signal starts.
        visited = set() 

        while minHeap:
            totalCost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            print("visiting node: ", node, " totalCost: ", totalCost)
            # why is it ending here? -- this is the only log line i'm seeing.
            visited.add(node)
            
            if len(visited) == n:
                return totalCost

            for nei, neiCost in adj[node]:
                if nei not in visited:
                    print("pushing neighboring node: ", nei, " with totalCost: ", neiCost, " to the heap.")
                    heapq.heappush(minHeap, (totalCost + neiCost, nei)) # this is really where the result building is happening 


        return -1
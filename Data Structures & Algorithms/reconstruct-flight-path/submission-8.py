class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # off bat, is this hierholzer's or something like that
        # given list of directed edges. need to reconstruct a path.
        # eulerian path?? -- is that when each edge is utilized exactly once? 
        # don't remember... 
        # we have the source node (JFK)

        # iirc there is some mechanism of like processing each edge and simulating a BFS layer by layer? -- nope I guess that's a different algorithm that I'm thinking of according to Claude 
        # just checked notion notes...walk until stuck, append, then unwind...
        # and then I think i might need to reverse the result
        # there are only up to 300 edges...so we can just iterate over them instead of building an adjacency list representation of the graph...this is a practical simplification 

        sorted_tickets = sorted(tickets) # process biggest lex. tickets first..
        # then when we reverse, smallest lex will be first

        path = [] 
        used_tickets = set() 
        def dfs(node):
            
            for i, (f, t) in enumerate(sorted_tickets):
                if i not in used_tickets and f == node:
                    # remove it? how do we make sure we're only using each ticket once. 
                    used_tickets.add(i)
                    dfs(t)  

            path.append(node)
        
        dfs("JFK")
        return path[::-1] # .reverse() returns None 







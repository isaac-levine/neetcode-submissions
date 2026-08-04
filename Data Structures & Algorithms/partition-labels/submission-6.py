class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

        # each letter must appear in only one substring
        
        # {char : lastIndex}
        last = {c : i for i, c in enumerate(s)} 



        # we want maximum number of groupings, but each character must be fully contained in only one grouping

        res = [] 

        l = 0
        while l < len(s):
            r = last[s[l]]
            i = l
            while i <= r:
                r = max(r, last[s[i]])
                i += 1 # can't do for loop because we're updating r inside the loop, and python evaluates the for loop condition once
            
            res.append(r - l + 1)
            l = r + 1
        
        return res
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {c : i for i, c in enumerate(s)} # it will overwrite as it goes so this is accurate

        res = []
        start = end = 0 

        for i in range(len(s)):
            c = s[i]

            # potentially have to update the end of our current window
            end = max(end, last[c])
            size = end - start + 1

            if i == end:
                res.append(size)
                start = i + 1
        
        return res
class Solution:

    def isPali(self, s):
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    # def isPali(self, s, l, r):
    #     while l < r:
    #         if s[l] != s[r]:
    #             return False
    #         l, r = l + 1, r - 1
    #     return True

    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy()) # might be in another recursive call making changes to this 
                return
            
            for j in range(i, len(s)):
                if self.isPali(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop() # clean up
                    # dfs(i + 1)

        dfs(0)
        return res


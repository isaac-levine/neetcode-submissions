class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def dfs(i, part):
            if i >= len(s):
                res.append(part[:])
                return 
            
            for j in range(i, len(s)): # iterate through every remaining position
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1, part)
                    part.pop() # cleanup

        dfs(0, [])
        return res 

    def isPalindrome(self, s: str, i: int, j: int):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        # feel like partitions are usually n-ary backtracking 

        res = [] 

        def backtrack(i, cur):
            if i == len(s):
                res.append(cur[:])
                return
            
            for j in range(i, len(s)):
                
                if self.isPalindrome(s, i, j):
                    cur.append(s[i : j + 1])
                    backtrack(j + 1, cur)
                    cur.pop()
        
        backtrack(0, [])
        return res

    def isPalindrome(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        # return all possible palindromic substrings --> off bat thinking backtracking ?
        # n-ary backtracking where you are trying to find a place to cut 

        res = [] 

        def backtrack(i, cur):
            if i == len(s):
                res.append(cur[::])
                return 
            
            for j in range(i, len(s)):
                if isPalindrome(s[i : j + 1]):
                    cur.append(s[i : j + 1])
                    backtrack(j + 1, cur)
                    
                    cur.pop()

        backtrack(0, []) # 
        return res
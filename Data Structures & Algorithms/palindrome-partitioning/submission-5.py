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

        res = [] 
        # backtracking? decisions do not appear to be cacheable 
        # recursive decision: do i cut this string here and add it to my list or do i extend it? 

        def backtrack(i: int, curSubstring: str, palindromes: List[str]):
            if i >= len(s):
                if not curSubstring:
                    res.append(palindromes[:])
                return
            
            curSubstring += s[i]
            # cut it here and add it if it's a palindrome 
            if isPalindrome(curSubstring):
                palindromes.append(curSubstring)
                backtrack(i + 1, "", palindromes)
                palindromes.pop() 
            
            # try to extend it
            backtrack(i + 1, curSubstring, palindromes)
        
        backtrack(0, "", [])
        return res
            



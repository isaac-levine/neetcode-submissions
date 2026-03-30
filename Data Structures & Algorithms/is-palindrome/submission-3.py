class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum() or s[l] == " ": # skip non-alphanumeric characters
                l += 1
            elif not s[r].isalnum() or s[r] == " ": # skip non-alphanumeric characters
                r -= 1
            elif s[l].lower() != s[r].lower():
                print(f"{s[l]} is not equal to {s[r]}")
                return False
            else:
                l += 1
                r -= 1

        return True

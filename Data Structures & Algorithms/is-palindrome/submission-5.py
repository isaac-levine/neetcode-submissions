class Solution:
    def isPalindrome(self, a: str) -> bool:

        l, r = 0, len(a) - 1

        while l < r:
            if not a[l].isalnum() or a[l] == " ": # skip non-alphanumeric characters
                l += 1
            elif not a[r].isalnum() or a[r] == " ": # skip non-alphanumeric characters
                r -= 1
            elif a[l].lower() != a[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True

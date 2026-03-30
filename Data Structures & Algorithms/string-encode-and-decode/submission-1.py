class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        print("encoded: ", res)
        return res

        

    def decode(self, s: str) -> List[str]:
        i = 0 # tells us what posiiton we're at in the input string so far
        res = []

        while i < len(s):
            j = i
            while s[j] != '#': # guaranteed to find one eventually
                j += 1
            length = int(s[i:j]) # this is the integer
            word = s[j + 1 : j + length + 1] # first char in the string itself to end of it
            res.append(word)
            i = j + 1 + length # move to end of this word

        return res

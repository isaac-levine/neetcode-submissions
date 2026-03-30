class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res 


    def decode(self, s: str) -> List[str]:
        i = 0 # where we are in the input string
        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : j + length + 1]
            res.append(word)
            i = j + 1 + length # move to the end of this word

        return res 

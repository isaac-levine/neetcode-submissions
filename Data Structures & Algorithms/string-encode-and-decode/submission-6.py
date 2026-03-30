class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # you need the # separator beacuse lengths can be more than one digit
        for s in strs:
            res += str(len(s)) + "#" + s 
        
        return res

    def decode(self, s: str) -> List[str]:
        res = [] 
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 # j is basically finding the end of this number
            length = int(s[i:j])
            i = j + 1
            j = i + length 
            res.append(s[i:j])
            i = j

        return res


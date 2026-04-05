class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digit_to_letters = {
            2 : ["A", "B", "C"],
            3 : ["D", "E", "F"],
            4 : ["G", "H", "I"],
            5 : ["J", "K", "L"],
            6 : ["M", "N", "O"],
            7 : ["P", "Q", "R", "S"],
            8 : ["T", "U", "V"],
            9 : ["W", "X", "Y", "Z"],
            0 : []
        }

        res = [] 

        if not digits:
            return res

        def dfs(i, cur):
            if i == len(digits):
                res.append("".join(cur[:]).lower())
                return

            digit = int(digits[i])

            # for digits[i], explore all paths (combinations)
            for letter in digit_to_letters[digit]:
                cur.append(letter)
                dfs(i + 1, cur)
                cur.pop()

        dfs(0, [])
        return res
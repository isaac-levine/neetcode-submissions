class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
        charCountsToAnagrams = defaultdict(list)
        for s in strs:
            charCounts = [0] * 26
            for c in s:
                charCounts[ord(c) - ord('a')] += 1
            charCountsToAnagrams[tuple(charCounts)].append(s)

        return list(charCountsToAnagrams.values())

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash = {}
        words = s.split()
        if len(words) != len(pattern): return False
        for i, word in enumerate(words):
            if pattern[i] in hash.keys():
                if hash.get(pattern[i]) != word:
                    return False
            else:
                if word in hash.values():
                    return False
                hash[pattern[i]] = word

        return True

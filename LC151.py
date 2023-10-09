class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = ""
        for i in range(len(words)-1, -1, -1):
            result += words[i]
            result += " "
        return result[:-1]
